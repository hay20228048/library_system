#In this file we are looking for:
    #Email uniqueness validation - Email must be unique
    #Member existence checks - Member must exist before update/delete
    #Business validation


from app.helper.exceptions import AlreadyExistsError, NotFoundError
from app.infrastructure.repositories.member_repository import (
    create_member, delete_member, get_all_members, get_member_by_email,
    get_member_by_id, update_member)


class MemberService:
    @staticmethod
    def add_member(data):
        #Validates unique email before creating (Check if email already exists)
        existing = get_member_by_email(data.get("email"))
        if existing:
            raise AlreadyExistsError(f"Email '{data.get('email')}' is already exists!")
        
        # If the email is Not exist: simply create a member  and returns the full member dictionary.
        member_id = create_member(data)
        return get_member_by_id(member_id)
    


    @staticmethod
    #Returns member if member_id exist or raises error if not.
    def get_member(member_id):
        member = get_member_by_id(member_id)
        if not member:
            raise NotFoundError(f"Member with ID {member_id} does not exist.")
        
        #if the member id exists, return the member info
        return member



    @staticmethod
    def get_all_members(limit=10, offset=0, search=None):

        if limit < 1 or offset<0:
            raise ValueError("Limit and offset must be positive")

        return get_all_members(limit, offset, search)



    @staticmethod
    def update_member(member_id, data):
        # If updating email, check uniqueness before updating.
        if "email" in data:
            existing = get_member_by_email(data.get("email"))
            #Here I have to check that the member id is already exist & the email is unique
            if existing and existing["member_id"] != member_id:
                raise AlreadyExistsError(f"Email '{data.get('email')}' is already exist.")

        updated = update_member(member_id, data)
        if not updated:
            raise NotFoundError(f"Member with ID {member_id} does not exist.")
        return updated

    @staticmethod
    def delete_member(member_id):
        deleted = delete_member(member_id)
        #if the deleted return value is False this means the member id does NOT exist in the table (Raises error if member not found)
        if not deleted:
            raise NotFoundError(f"Member with ID {member_id} does not exist.")
        return True
