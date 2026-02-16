#test_book_repository.py
from app.infrastructure.repositories.book_repository import *

# Create book
book_id = create_book({
    "title": "Essential SQLAlchemy: Mapping Python to Databases",
    "author": "Jason Myers, Rick Copeland"
})

print("Created Book ID:", book_id)

# Get book
book = get_book_by_id(book_id)
print("Book:", book)

# Borrow book
borrowed = borrow_book(book_id, "75bd9bc5-a006-4af2-bb85-f04058544468")
print("Borrowed:", borrowed)

# Return book
returned = return_book(book_id)
print("Returned:", returned)
