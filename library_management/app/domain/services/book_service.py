#In this file we are looking for:
    #Borrow rules: Borrow book validation 
    #Return rules: Return book logic - Member must exist and the member has already borrow the book
    #Book availability checks - Book must exist before update/delete
    #Business validation - Member must exist

#Borrowing Rules
    #Book must exist
    #Book cannot already be borrowed
    #Member must exist
    #Updates borrowed_by + borrowed_date automatically

#Returning Rules
    #Book must exist
    #Book must be currently borrowed
    #Resets borrowed_by + borrowed_date

from app.helper.exceptions import BorrowError, NotFoundError
from app.infrastructure.repositories.book_repository import (borrow_book,
                                                             create_book,
                                                             delete_book,
                                                             get_all_books,
                                                             get_book_by_id,
                                                             return_book,
                                                             update_book)
from app.infrastructure.repositories.member_repository import get_member_by_id


class BookService:
    @staticmethod
    def add_book(data):
        book_id = create_book(data)
        return get_book_by_id(book_id)

    @staticmethod
    def get_book(book_id):
        book = get_book_by_id(book_id)
        if not book:
            raise NotFoundError(f"Book with ID {book_id} does not exist.")
        return book
    

    @staticmethod
    def get_all_books(limit=10, offset=0, search=None):

        if limit < 1 or offset<0 :
            raise ValueError("Limit and offset must be +ve #")

        return get_all_books(limit, offset, search)


    @staticmethod
    def update_book(book_id, data):
        updated = update_book(book_id, data)
        if not updated:
            raise NotFoundError(f"Book with ID {book_id} does not exist.")
        return updated

    @staticmethod
    def delete_book(book_id):
        deleted = delete_book(book_id)
        if not deleted:
            raise NotFoundError(f"Book with ID {book_id} does not exist.")
        return True

    @staticmethod
    def borrow_book(book_id, member_id):
        # Validate book existence
        book = get_book_by_id(book_id)
        if not book:
            raise NotFoundError(f"Book with ID {book_id} does not exist.")

        #Check if book is already borrowed
        if book["is_borrowed"]:
            raise BorrowError(f"Book '{book['title']}' is already borrowed.")

        # Validate member existence
        member = get_member_by_id(member_id)
        if not member:
            raise NotFoundError(f"Member with ID {member_id} does not exist.")

        # Borrow book
        updated_book = borrow_book(book_id, member_id)
        return updated_book

    @staticmethod
    def return_book(book_id):
        # Validate book existence
        book = get_book_by_id(book_id)
        if not book:
            raise NotFoundError(f"Book with ID {book_id} does not exist.")

        # Check if book is actually borrowed
        if not book["is_borrowed"]:
            raise BorrowError(f"Book '{book['title']}' is not currently borrowed.")

        updated_book = return_book(book_id)
        return updated_book
