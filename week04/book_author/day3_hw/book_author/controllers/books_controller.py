from flask import redirect, request, render_template, Blueprint
from repositories import book_repository
from repositories import author_repository

from models.book import Book
import pdb

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/")
def index():
    return render_template("index.html")

# select_all() to view all books
@books_blueprint.route("/books")
def select_all():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

# select(id)
@books_blueprint.route("/books/<index>")
def books_show(index):
    one_book = book_repository.select(index)
    return render_template("books/show.html", book=one_book, index=index)

# delete one book
@books_blueprint.route("/books/delete/<index>", methods=["POST"])
def books_delete(index):
    book_repository.delete(index)
    return redirect("/books")

# # create a book
@books_blueprint.route("/books", methods=["POST"])
def books_create():
    title = request.form["title"]
    author = request.form["author_id"]
    genre = request.form["genre"]
    pdb.set_trace()
    new_book = Book(title, author, genre)
    book_repository.save(new_book)
    return redirect("/books")


@books_blueprint.route("/books/new")
def books_new():
    return render_template("books/new.html")




# @app.route("/books/<index>", methods=["POST"])
# # route works with route name and methods - line18 is not connected to this one
# # as its route is ["GET"]
# def books_update(index):
#     book = books[int(index)]
#     checked_out = "checked_out" in request.form
#     # line 48 is to check if "checked-out" exist as when it is not checked there is no name="checked_out"
#     book.toggle_check_out(checked_out)
#     return redirect("/books/" + index)
