
from models.book import *

book1 = Book("Norwegian Wood", "Haruki Murakami", "literary fiction", False)
book2 = Book("The Devotion of Suspect X", "Keigo Higashono", "Crime", False)
book3 = Book("Diary of a Mademan", "Lu Xun", "fiction", True)

books = [book1, book2, book3]

def add_book(new_book):
    books.append(new_book)

def delete_book(index):
    del books[index]



