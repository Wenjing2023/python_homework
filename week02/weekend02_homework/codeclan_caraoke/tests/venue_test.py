import unittest
from src.room import Room
from src.guest import Guest
from src.venue import Venue
from src.bar import Bar


class TestVenue(unittest.TestCase):
    def setUp(self):
        self.venue = Venue("CC_Karaoke", 1000)
        self.room = Room("Room e63", 24, 70)
        self.guest_1 = Guest("Wenjing", 50, "Bohemian Rhapsody")
        self.guest_2 = Guest("Aneeqa", 100, "what's up")
        self.guest_3 = Guest("Sarah", 80, "Yellow")
        self.beer = Bar("beer", 5, 2)

    def test_venue_has_name(self):
        self.assertEqual("CC_Karaoke", self.venue.name)

    def test_venue_has_money(self):
        self.assertEqual(1000, self.venue.till)

    def test_guest_can_afford_to_enter(self):
        self.assertEqual(
            True, self.venue.guest_can_afford_to_enter(self.guest_2, self.room)
        )

    def test_guest_cannot_afford_to_enter(self):
        self.assertEqual(
            False, self.venue.guest_can_afford_to_enter(self.guest_1, self.room)
        )

    def test_check_in_guest(self):
        self.assertEqual(1000, self.venue.till)
        self.venue.check_in_guest(self.guest_3, self.room)
        self.assertEqual(1070, self.venue.till)
        self.venue.check_in_guest(self.guest_2, self.room)
        self.assertEqual(1140, self.venue.till)
        self.assertEqual(2, self.venue.guests_count())
        # self.assertEqual(1140, self.venue.till)

    def test_allocate_guest(self):
        self.venue.check_in_guest(self.guest_3, self.room)
        self.venue.check_in_guest(self.guest_2, self.room)
        self.room.add_guest(self.guest_3)
        self.assertEqual(2, self.venue.guests_count())
        self.assertEqual(1, self.room.guests_count())

    def test_check_out_guest(self):
        self.venue.check_in_guest(self.guest_3, self.room)
        self.venue.check_in_guest(self.guest_2, self.room)
        # self.venue.increase_till_check_in(self.room)
        self.assertEqual(1140, self.venue.till)
        self.room.add_guest(self.guest_3)
        self.room.remove_guest(self.guest_3)
        self.venue.check_out_guest(self.guest_3)
        self.assertEqual(1, self.venue.guests_count())
        self.assertEqual(0, self.room.guests_count())

    def test_can_provide_bar_service(self):
        self.assertEqual(1000, self.venue.till)
        self.assertEqual(0, len(self.venue.guest))
        self.assertEqual(80, self.guest_3.money)
        self.venue.check_in_guest(self.guest_3, self.room)
        self.guest_3.enter(self.room)
        # Q: Why this does not work - venue, increase_till_check_in is wrong
        # self.venue.increase_till_check_in(self.room)
        # self.assertEqual(1070, self.venue.till)
        self.assertEqual(1, len(self.venue.guest))
        self.assertEqual(10, self.guest_3.money)
        # self.assertEqual(self.guest_3.buy_food(self.room, self.beer))
