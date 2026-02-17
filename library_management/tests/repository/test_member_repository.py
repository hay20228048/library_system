from app.infrastructure.repositories.member_repository import (
    create_member, delete_member, get_all_members, get_member_by_id,
    update_member)

# Create member
member_id = create_member({
    "name": "Haya",
    "email": "haya@gmaill.com"
})

print("Created Member:", member_id)

# Get member
member = get_member_by_id(member_id)
print("Member:", member)

# Update member
updated = update_member(member_id, {"name": "Haya Updated"})
print("Updated:", updated)

# Get all members
members = get_all_members()
print("All Members:", members)

# Delete member
deleted = delete_member(member_id)
print("Deleted:", deleted)
