from db.run_sql import run_sql
import pdb

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, author_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.genre]
    results = run_sql(sql, values)
    id = results[0]["id"]
    book.id = id
    return book

def select_all():
    sql = "SELECT * FROM books"
    books = []
    results = run_sql(sql)
    for row in results:
        author = author_repository.select(row["author_id"])
        book = Book(row["title"], author, row["genre"], row["id"])
        books.append(book)
    return books

def select(id):
    sql = "SELECT * FROM books WHERE id = %s"
    book = None
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        author = author_repository.select(result["author_id"])
        book = Book(result["title"], author, result["genre"], result["id"])
    return book

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(book):
    sql = "UPDATE books SET (title, artist_id, genre) = (%s, %s, %s) WHERE id = %s"
    values = [book.title, book.author.id, book.genre, book.id]
    run_sql(sql, values)