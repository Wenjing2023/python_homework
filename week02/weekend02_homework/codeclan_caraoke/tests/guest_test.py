import unittest
from src.room import Room
from src.guest import Guest
from src.bar import Bar
from src.venue import Venue


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.venue = Venue("CC_Karaoke", 1000)
        self.guest_1 = Guest("Wenjing", 50, "Bohemian Rhapsody")
        self.guest_2 = Guest("Aneeqa", 100, "what's up")
        self.room = Room("room_e63", 24, 70)
        self.beer = Bar("beer", 5, 2)
        self.burger = Bar("Burger", 10, 20)

    def test_guest_has_name(self):
        self.assertEqual("Wenjing", self.guest_1.name)

    def test_guest_has_money(self):
        self.assertEqual(100, self.guest_2.money)

    def test_guest_has_fav_song(self):
        self.assertEqual("what's up", self.guest_2.favourite_song)

    def test_sufficient_funds_true_if_enough(self):
        self.assertEqual(True, self.guest_2.sufficient_funds_to_enter(self.room))

    def test_sufficient_funds_false_if_not_enough(self):
        self.assertEqual(False, self.guest_1.sufficient_funds_to_enter(self.room))

    def test_enter_decrease_money(self):
        self.guest_2.enter(self.room)
        self.assertEqual(30, self.guest_2.money)

    def test_fav_song(self):
        self.room.add_songs("Bohemian Rhapsody")
        self.assertEqual("Whoo!", self.room.fav_song(self.guest_1.favourite_song))
        self.assertEqual("Boooo!", self.room.fav_song(self.guest_2.favourite_song))

    def test_sufficient_funds_for_bar_true_if_enough(self):
        self.guest_2.enter(self.room)
        self.assertEqual(
            True, self.guest_2.sufficient_funds_for_bar(self.room, self.beer)
        )

    def test_sufficient_funds_for_bar_false_if_not_enough(self):
        poor_guest = Guest("Dani", 74, "Sugar Man")
        poor_guest.enter(self.room)
        self.assertEqual(
            False, poor_guest.sufficient_funds_for_bar(self.room, self.beer)
        )

    def test_buy_food(self):
        self.guest_2.enter(self.room)
        self.guest_2.buy_food(self.room, self.beer)
        self.guest_2.buy_food(self.room, self.burger)
        self.assertEqual(15, self.guest_2.money)

    # def test_cannot_buy_food_out_of_stock():
