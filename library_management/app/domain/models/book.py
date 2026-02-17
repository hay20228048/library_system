#Books Table
    #book_id (Primary Key)
    #title
    #author
    #is_borrowed
    #borrowed_date
    #borrowed_by (FK → members)


from app.infrastructure.db import metadata
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        Table)

books = Table(
    "books",
    metadata,
    Column("book_id", Integer, primary_key=True), #The unique identifier for the book.
    Column("title", String, nullable=False), #The title of the book.
    Column("author", String, nullable=False), #The author of the book.
    Column("is_borrowed", Boolean, default=False), #A flag indicating if the book is currently borrowed or available.
    Column("borrowed_date", DateTime, nullable=True), #The date when the book was borrowed.
    Column("borrowed_by", String, ForeignKey("members.member_id"), nullable=True) #The ID of the member who borrowed the book (foreign key to the members table).

)
