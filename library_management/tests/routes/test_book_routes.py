#Book Routes Test Suite
import uuid


def create_member(client):
    return client.post("/members/", json={
        "name": "Borrow User",
        "email": f"{uuid.uuid4()}@test.com"
    }).get_json()


def create_book(client):
    return client.post("/books/", json={
        "title": "Test Book",
        "author": "Author"
    }).get_json()


#Create Book
def test_create_book(client):
    response = client.post("/books/", json={
        "title": "Flask Book",
        "author": "Author"
    })
    assert response.status_code == 201


#Get Books
def test_get_books(client):
    response = client.get("/books/")
    assert response.status_code == 200


#Get Book By ID
def test_get_book_by_id(client):
    book = create_book(client)
    response = client.get(f"/books/{book['book_id']}")
    assert response.status_code == 200


#Update Book
def test_update_book(client):
    book = create_book(client)
    response = client.put(
        f"/books/{book['book_id']}",
        json={"title": "Updated Book"}
    )
    assert response.status_code == 200


#Delete Book
def test_delete_book(client):
    book = create_book(client)
    response = client.delete(f"/books/{book['book_id']}")
    assert response.status_code == 200


#Borrow Book
def test_borrow_book(client):
    member = create_member(client)
    book = create_book(client)
    response = client.post(
        f"/books/borrow/{book['book_id']}/{member['member_id']}"
    )
    assert response.status_code == 200
    assert response.get_json()["is_borrowed"] is True


def test_borrow_already_borrowed_book(client):

    member = client.post("/members/", json={
        "name": "User1",
        "email": "user1@test.com"
    }).get_json()

    book = client.post("/books/", json={
        "title": "Borrow Test",
        "author": "Author"
    }).get_json()

    # First borrow
    client.post(f"/books/borrow/{book['book_id']}/{member['member_id']}")

    # Second borrow attempt
    response = client.post(
        f"/books/borrow/{book['book_id']}/{member['member_id']}"
    )

    assert response.status_code == 400



#Return Book
def test_return_book(client):
    member = create_member(client)
    book = create_book(client)
    client.post(
        f"/books/borrow/{book['book_id']}/{member['member_id']}"
    )
    response = client.post(f"/books/return/{book['book_id']}")
    assert response.status_code == 200
    assert response.get_json()["is_borrowed"] is False


def test_borrow_non_existing_book(client):

    member = client.post("/members/", json={
        "name": "User",
        "email": "borrowmissing@test.com"
    }).get_json()

    response = client.post(
        f"/books/borrow/999/{member['member_id']}"
    )
    assert response.status_code == 404
