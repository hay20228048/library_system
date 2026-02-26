from app.infrastructure.kafka.producer import publish_event
import time

TOPIC = "book-events"


def book_created_event(book):
    event = {
        "event_type": "BOOK_CREATED",
        "book_id": book["book_id"],
        "title": book["title"],
        "author": book["author"],
        "timestamp": time.time(),
    }

    publish_event(TOPIC, event)


def book_updated_event(book):
    event = {
        "event_type": "BOOK_UPDATED",
        "book_id": book["book_id"],
        "title": book["title"],
        "author":  book["author"],
        "timestamp": time.time(),
    }

    publish_event(TOPIC, event)


 
def book_deleted_event(book_id: int):
    event = {
        "event_type": "BOOK_DELETED",
        "book_id": book_id,
        "timestamp": time.time(),
    }

    publish_event(TOPIC, event)


def book_borrowed_event(book, member_id):
    event = {
        "event_type": "BOOK_BORROWED",
       "book_id": book["book_id"],
        "member_id": member_id,
        "timestamp": time.time(),
    }

    publish_event(TOPIC, event)