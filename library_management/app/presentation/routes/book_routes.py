# POST	/books
# GET	/books
# GET	/books/{id}
# PUT	/books/{id}
# DELETE	/books/{id}
# POST	/borrow/{book_id}/{member_id}
# POST	/return/{book_id}


from app.domain.services.book_service import BookService
from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from app.presentation.models.book_model import BookCreate, BookUpdate

book_bp = Blueprint("book_bp", __name__)


# Create Book
@book_bp.route("/", methods=["POST"])
def add_book():
    try:
        data = BookCreate(**request.json)
        book = BookService.add_book(title=data.title, author=data.author)
        return jsonify(book), 201

    except ValidationError as err:
        return {"error": err.messages}, 400


# Get All Books
@book_bp.route("/", methods=["GET"])
def get_books():

    limit = int(request.args.get("limit", 10))
    offset = int(request.args.get("offset", 0))
    search = request.args.get("search")
    books = BookService.get_all_books(limit, offset, search)
    return jsonify(books), 200


# Get Book by ID
@book_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = BookService.get_book(book_id)
    return jsonify(book), 200


# Update Book
@book_bp.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    try:
        data = BookUpdate(**request.json)

        updated = BookService.update_book(book_id, **data.dict(exclude_unset=True))
        return jsonify(updated), 200

    except ValidationError as err:
        return {"error": err.messages}, 400


# Delete Book
@book_bp.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    BookService.delete_book(book_id)
    return jsonify({"message": "Book deleted successfully"}), 200


# Borrow Book
@book_bp.route("/borrow/<int:book_id>/<member_id>", methods=["POST"])
def borrow_book(book_id, member_id):
    book = BookService.borrow_book(book_id, member_id)
    return jsonify(book), 200


# Return Book
@book_bp.route("/return/<int:book_id>", methods=["POST"])
def return_book(book_id):
    book = BookService.return_book(book_id)
    return jsonify(book), 200
