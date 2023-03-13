import unittest

from src.song import Song
from src.room import Room


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Bohemian Rhapsody", "Queen")
        self.song_2 = Song("Hello", "Adele")
        self.room = Room("Room e63", 24, 70)

    def test_song_has_name(self):
        self.assertEqual("Bohemian Rhapsody", self.song_1.name)

    def test_song_has_singer(self):
        self.assertEqual("Adele", self.song_2.singer)

    def test_add_songs_to_rooms(self):
        self.room.add_songs(self.song_1)
        self.assertEqual(1, self.room.songs_count())
