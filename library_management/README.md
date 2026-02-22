# Library Management System

A simple backend system built with Flask, PostgreSQL, and SQLAlchemy Core to manage books and library members.

## Main Features

- Manage Books (CRUD Operation: Create, Read, Update, Delete)
- Manage Members (CRUD Operation: Create, Read, Update, Delete)
- Borrow and Return Books
- Pagination & Search
- Input Validation(Pydantic)
- Global Error Handling
- Pytest Test Suite

## Run Project

```bash
#Clone Repository
git clone <repo-url>
cd library_management

docker compose up
```

#Uvicorn running on http://0.0.0.0:8000

## Main Endpoints

### Books

```
POST   /books/
GET    /books/
PUT    /books/{book_id}
DELETE /books/{book_id}
POST   /books/borrow/{book_id}/{member_id}
POST   /books/return/{book_id}
```

### Members

```
POST   /members/
GET    /members/
PUT    /members/{member_id}
DELETE /members/{member_id}
```

## Note: for the complete documentation, you can view the Documentation file in this project
