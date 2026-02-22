#Members Table
    #member_id (UUID)
    #name
    #email (Unique)


import uuid

from sqlalchemy import Column, String, Table

from app.infrastructure.db import metadata

members = Table(
    "members",
    metadata,
    Column("member_id", String, primary_key=True, default=lambda: str(uuid.uuid4())), #The unique identifier for the member.
    Column("name", String, nullable=False), #The name of the member.
    Column("email", String, unique=True, nullable=False) #The email of the member (must be unique).
)
