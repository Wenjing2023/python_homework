import unittest

from models.book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("Norwegian Wood", "Haruki Murakami", "literary fiction", True)
        self.book2 = Book("The Devotion of Suspect X", "Keigo Higashono", "Crime", False)
        self.book3 = Book("Diary of a Mademan", "Lu Xun", "fiction", True)

        self.books = [self.book1, self.book2, self.book3]

        self.new_book = ("The Little Prince", "Antoine de Saint-Exupéry", "Children's literature")

    def test_add_book(self):
        self.book.add_book(self.new_book)
        self.assertEqual(4,len(self.books))
    
    def test_delete_book(self):
        self.book.delete_book(1)
        self.assertEqual(2,len(self.books))