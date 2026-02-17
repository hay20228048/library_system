from typing import Optional

from pydantic import BaseModel, EmailStr


class MemberCreate(BaseModel):
    name: str
    email: EmailStr


class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
