from flask import redirect, request, render_template
from app import app
from models.book import Book
from models.books import *


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def books_index():
    return render_template("books/index.html", books=books)


@app.route("/books/<index>")
def books_show(index):
    book = books[int(index)]
    return render_template("books/show.html", book=book, index=index)


@app.route("/books", methods=["GET","POST"])
def books_create():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre, False)
    add_book(new_book)
    return redirect("/books")


@app.route("/books/new")
def books_new():
    return render_template("books/new.html")


@app.route("/books/delete/<index>", methods=["POST"])
# why when I click delete, books/delete/<index> did not shhow
def books_delete(index):
    delete_book(int(index))
    return redirect("/books")


# @app.route("/books/<index>", methods=["POST"])
# def books_update(index):
#     book = books[int(index)]
#     checked_out = "checked_out" in request.form
#     book.toggle_check_out(checked_out)
#     return redirect("/books/" + index)

# Book is already checked out; to check in a book:
@app.route("/books/<index>", methods=["POST"])
def books_check_status(index):
    book = books[int(index)]
    if "checked-in" in request.form:
        book.checked_out == False
    elif  "checked-out" in request.form:
        book.checked_out == True

    return redirect("/books")

