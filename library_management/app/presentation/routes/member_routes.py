# This file handles HTTP requests related to members.
#
# #POST	/members
# GET	/members
# GET	/members/{id}
# PUT	/members/{id}
# DELETE	/members/{id}


from typing import Optional

from fastapi import APIRouter, Body, Query
from pydantic import EmailStr, ValidationError

from app.domain.services.member_service import MemberService
from app.presentation.models.member_model import MemberCreate, MemberUpdate

# Creates route group named member_bp to be registerd inside main.py.
router = APIRouter()


# Create Member
@router.post("/", response_model=dict, status_code=201)
def add_member(member: MemberCreate = Body(...)):
    return MemberService.add_member(member)


# Get All Members
@router.get("/", response_model=list)
def get_members(
    limit: int = Query(10, ge=0),
    offset: int = Query(0, ge=0),
    search: Optional[str] = None,
):
    return MemberService.get_all_members(limit=limit, offset=offset, search=search)


# FastAPI automatically validates path parameters using type hints.
# Get Member by ID
@router.get("/{member_id}", response_model=dict)
def get_member(member_id: str):
    return MemberService.get_member(member_id)


# Update Member
@router.put("/{member_id}", response_model=dict)
def update_member(member_id: str, member: MemberUpdate = Body(...)):
    return MemberService.update_member(member_id, member)


# Delete Member
@router.delete("/{member_id}")
def delete_member(member_id: str):
    MemberService.delete_member(member_id)
    return {"message": "Member deleted successfully"}
