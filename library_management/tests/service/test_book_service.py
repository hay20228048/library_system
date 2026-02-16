from app.domain.services.member_service import MemberService
from app.domain.services.book_service import BookService


# Add book
book = BookService.add_book({"title": "Python", "author": "Haya"})
print("Added Book:", book)

# Borrow book with non-existent member
try:
    BookService.borrow_book(book["book_id"], "fake-member-id")
except ValueError as e:
    print("Borrow with invalid member:", e)

# Add valid member and borrow
valid_member = MemberService.add_member({"name": "Haya", "email": "haya@test3.com"})
borrowed_book = BookService.borrow_book(book["book_id"], valid_member["member_id"])
print("Borrowed Book:", borrowed_book)

# Attempt to borrow already borrowed book
try:
    BookService.borrow_book(book["book_id"], valid_member["member_id"])
except ValueError as e:
    print("Borrow already borrowed:", e)

# Return book
returned_book = BookService.return_book(book["book_id"])
print("Returned Book:", returned_book)
