from db.run_sql import run_sql
import pdb
from models.book import Book
from models.author import Author


def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    author.id= id
    return author

# to select all so when click "books" we can see them all "/books"
def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)
    for row in results:
        author = Author(row["name"], row["id"])
        authors.append(author)
    return authors


def select(id):
    sql = "SELECT * FROM authors WHERE id = %s"
    author = None
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        author = Author(result["name"],result["id"] )
    return author

