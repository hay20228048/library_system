#Member Routes Test Suite


import uuid


#To avoid duplicates each time
def generate_email():
    return f"{uuid.uuid4()}@test.com"


#Create Member
def test_create_member(client):
    response = client.post("/members/", json={
        "name": "Test User",
        "email": generate_email()
    })
    assert response.status_code == 201 #201 status code means a new resource was created from the request. 
    assert "member_id" in response.get_json()


#Get All Members
def test_get_members(client):

    response = client.get("/members/")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


#Get Member By ID
def test_get_member_by_id(client):
    member = client.post("/members/", json={
        "name": "Find User",
        "email": generate_email()
    }).get_json()
    response = client.get(f"/members/{member['member_id']}")
    assert response.status_code == 200
    assert response.get_json()["member_id"] == member["member_id"]


#Update Member
def test_update_member(client):
    member = client.post("/members/", json={
        "name": "Update User",
        "email": generate_email()
    }).get_json()
    response = client.put(
        f"/members/{member['member_id']}",
        json={"name": "Updated Name"}
    )
    assert response.status_code == 200
    assert response.get_json()["name"] == "Updated Name"


#Delete Member
def test_delete_member(client):
    member = client.post("/members/", json={
        "name": "Delete User",
        "email": generate_email()
    }).get_json()
    response = client.delete(f"/members/{member['member_id']}")
    assert response.status_code == 200



#Delete-non existing member
def test_delete_non_existing_member(client):

    response = client.delete("/members/non-existing-id")

    assert response.status_code == 404



def test_duplicate_member_email(client):

    client.post("/members/", json={
        "name": "User",
        "email": "duplicate@test.com"
    })

    response = client.post("/members/", json={
        "name": "User2",
        "email": "duplicate@test.com"
    })

    assert response.status_code == 400
