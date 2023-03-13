import unittest

from src.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("room_e63", 24, 70)
        self.guest = []

    def test_room_has_name(self):
        self.assertEqual("room_e63", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(24, self.room.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(70, self.room.entry_fee)

    def test_too_many_guests_true_when_over_capacity(self):
        if len(self.guest) == 25:
            self.assertEqual(True, self.room.too_many_guests())

    def test_too_many_guests_false_when_under_capacity(self):
        if len(self.guest) == 20:
            self.assertEqual(False, self.room.too_many_guests())
