from alembic import op
import sqlalchemy as sa
from config.enums.role import RoleEnum
from datetime import datetime


def create_users_table():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("username", sa.String(50), unique=True, nullable=False, index=True),
        sa.Column("email", sa.String, unique=True, nullable=False, index=True),
        sa.Column("password", sa.String, nullable=False),
        sa.Column("image", sa.String, nullable=False),
        sa.Column(
            "role",
            sa.Enum(RoleEnum),
            nullable=False,
            index=True,
        ),
        sa.Column("address", sa.String, nullable=False),
        sa.Column("phone", sa.String, unique=True, nullable=False, index=True),
        sa.Column(
            "created_at",
            sa.DateTime,
            nullable=False,
            default=datetime.now(),
            index=True,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            default=datetime.now(),
            onupdate=datetime.now(),
        ),
    )


def remove_users_table():
    op.drop_table("users")
    op.execute("DROP TYPE IF EXISTS roleenum")
