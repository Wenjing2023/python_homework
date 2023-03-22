import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

# book_1 = Book("The Lord of the Rings", "J R R Tolkien", "fantasy", True)
# book_2 = Book("The Hobbit", "J R R Tolkien", "fantasy", False)
# book_3 = Book("Clean Clode", "Robert Martin", "software development", True)

author1 = Author("J R R Tolkien")
author_repository.save(author1)

book1 = Book("The Lord of the Rings", author1, "fantasy")
book_repository.save(book1)
book2 = Book("The Hobbit", author1, "fantasy")
book_repository.save(book2)

print(book1.title + book2.author.name)

author_repository.select_all()
book_repository.select_all()


