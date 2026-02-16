#-------------------------#
#Main Functions:
#create_book()
#get_book_by_id()
#get_all_books()
#update_book()
#delete_book()
#borrow_book()
#return_book()
#-------------------------#

from sqlalchemy import insert,select, delete, update, or_
from sqlalchemy.exc import SQLAlchemyError
from app.domain.models.book import books
from app.infrastructure.db import get_connection
from app.helper import help_function
from datetime import datetime

#disable SQLAlchemy INFO logs for cleaner output
import logging
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

#Create Book
#Adds a new book.
def create_book(data):
    conn = get_connection()
    try:
        stmt = insert(books).values(**data)
        result = conn.execute(stmt)
        conn.commit()

        return result.inserted_primary_key[0] # return book_id
    
    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer

    finally:
        conn.close()


#Get Book By ID 
#Fetches single book.
def get_book_by_id(book_id):
    conn = get_connection()
    try:
        stmt = select(books).where(books.c.book_id == book_id)
        result = conn.execute(stmt).fetchone()

        return help_function.row_to_dict(result) #Returning Dictionary OR None
    
    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer

    finally:
        conn.close()



#Get All Books
#Fetches all books: Pagination + Search
def get_all_books(limit=10, offset=0, search=None):
    conn = get_connection()
    try:
        query = select(books)

        #Search
        if search:
            query = query.where(
            or_(#ilike : case insensitive search
            books.c.title.ilike(f"%{search}%"),
            books.c.author.ilike(f"%{search}%")
                    )
                )
        #Pagination
        query = query.limit(limit).offset(offset)
        result = conn.execute(query)
        return [help_function.row_to_dict(row) for row in result] #Returning List of dictionaries

    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer
   
    finally:
        conn.close()


#Update Book
def update_book(book_id, data):
    conn = get_connection()
    try:
        stmt = (
            update(books)
            .where(books.c.book_id == book_id)
            .values(**data)
            .returning(books)
        )
        result = conn.execute(stmt).fetchone()
        conn.commit()
        return help_function.row_to_dict(result) #Returning Updated book object
     
    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer

 
    finally:
        conn.close()



#Delete Book
def delete_book(book_id):
    conn = get_connection()
    try:
        stmt = delete(books).where(books.c.book_id == book_id)
        result = conn.execute(stmt)
        conn.commit()
        return result.rowcount > 0 #Returning True or False
     
    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer

    finally:
        conn.close()


#Borrow Book
#Resets borrowing fields.
def borrow_book(book_id, member_id):
    print("****"*10, member_id)
    conn = get_connection()
    try:
        stmt = (
            update(books)
            .where(books.c.book_id == book_id)
            .values(
                is_borrowed=True,
                borrowed_by=member_id,
                borrowed_date=datetime.utcnow()
            )
            .returning(books)
        )
        result = conn.execute(stmt).fetchone()
        conn.commit()
        return help_function.row_to_dict(result)
    
    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer


    finally:
        conn.close()


# Return Book
def return_book(book_id):
    conn = get_connection()
    try:
        stmt = (
            update(books)
            .where(books.c.book_id == book_id)
            .values(
                is_borrowed=False,
                borrowed_by=None,
                borrowed_date=None
            )
            .returning(books)
        )

        result = conn.execute(stmt).fetchone()
        conn.commit()

        return help_function.row_to_dict(result)
    
    except SQLAlchemyError as e:
        conn.rollback()
        raise  # Propagate exception to service layer

    finally:
        conn.close()
