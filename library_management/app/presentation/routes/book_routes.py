# POST	/books
# GET	/books
# GET	/books/{id}
# PUT	/books/{id}
# DELETE	/books/{id}
# POST	/borrow/{book_id}/{member_id}
# POST	/return/{book_id}


from app.domain.services.book_service import BookService
from fastapi import APIRouter, Query, Body
from typing import Optional
from pydantic import ValidationError
from app.presentation.models.book_model import BookCreate, BookUpdate

router = APIRouter()


# Create Book
@router.post("/", response_model=dict, status_code=201)
def add_book(book: BookCreate = Body(...)):
    try:
        book = BookService.add_book(book)
        return book

    except ValidationError as err:
        return {"error": err.messages}, 400


# Get All Books
@router.get("/")
def get_books(
    # ge=0 ensures limit and offset are ≥0.
    limit: int = Query(10, ge=0),
    offset: int = Query(0, ge=0),
    search: Optional[str] = None,
):
    books = BookService.get_all_books(limit=limit, offset=offset, search=search)
    return books


# Get Book by ID
@router.get("/{book_id}")
def get_book(book_id: int):
    book = BookService.get_book(book_id)
    return book


# exclude_unset=True ensures only provided fields are updated.
@router.put("/{book_id}")
def update_book(book_id: int, book: BookUpdate = Body(...)):
    updated = BookService.update_book(book_id, book)
    return updated


@router.delete("/{book_id}")
def delete_book(book_id: int):
    BookService.delete_book(book_id)
    return {"message": "Book deleted successfully"}


# Borrow Book
@router.post("/borrow/{book_id}/{member_id}")
def borrow_book(book_id: int, member_id: str):
    book = BookService.borrow_book(book_id, member_id)
    return book


# Return Book
@router.post("/return/{book_id}")
def return_book(book_id: int):
    book = BookService.return_book(book_id)
    return book
