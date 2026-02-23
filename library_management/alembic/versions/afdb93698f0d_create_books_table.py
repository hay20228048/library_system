"""create books table

Revision ID: afdb93698f0d
Revises:
Create Date: 2026-02-23 10:07:55.429334

"""

from alembic import op
import sqlalchemy as sa
import uuid

# revision identifiers, used by Alembic.
revision = "afdb93698f0d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "members",
        sa.Column(
            "member_id", sa.String, primary_key=True, default=lambda: str(uuid.uuid4())
        ),  # The unique identifier for the member.
        sa.Column("name", sa.String, nullable=False),  # The name of the member.
        sa.Column("email", sa.String, unique=True, nullable=False),
    )


def downgrade():
    op.drop_table("members")
