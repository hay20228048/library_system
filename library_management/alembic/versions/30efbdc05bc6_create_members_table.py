"""create members table

Revision ID: 30efbdc05bc6
Revises: afdb93698f0d
Create Date: 2026-02-23 12:18:24.767367

"""

from alembic import op
import sqlalchemy as sa
import uuid

# revision identifiers, used by Alembic.
revision = "30efbdc05bc6"
down_revision = "afdb93698f0d"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "books",
        sa.Column(
            "book_id", sa.Integer, primary_key=True
        ),  # The unique identifier for the book.
        sa.Column("title", sa.String, nullable=False),  # The title of the book.
        sa.Column("author", sa.String, nullable=False),  # The author of the book.
        sa.Column(
            "is_borrowed", sa.Boolean, default=False
        ),  # A flag indicating if the book is currently borrowed or available.
        sa.Column(
            "borrowed_date", sa.DateTime, nullable=True
        ),  # The date when the book was borrowed.
        sa.Column(
            "borrowed_by", sa.String, sa.ForeignKey("members.member_id"), nullable=True
        ),  # The ID of the member who borrowed the book (foreign key to the members table).
    )


def downgrade():
    op.drop_table("books")
