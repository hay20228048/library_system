from app.domain.services.member_service import MemberService

# Add member
member = MemberService.add_member({"name": "Ana", "email": "anav@test.com"})
print("Added Member:", member)

# Attempt duplicate email
try:
    MemberService.add_member({"name": "Alice 2", "email": "alice@ftest.com"})
except ValueError as e:
    print("Duplicate email error caught:", e)



# Update member
updated_member = MemberService.update_member(member["member_id"], {"name": "Alice Updated"})
print("Updated Member:", updated_member)

# Delete member
MemberService.delete_member(member["member_id"])
print("Member deleted successfully")



