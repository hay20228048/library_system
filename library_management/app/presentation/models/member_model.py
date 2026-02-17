from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID


class MemberCreate(BaseModel):
    name: str
    email: EmailStr


class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
