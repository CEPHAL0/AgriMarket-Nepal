from alembic import op
import sqlalchemy as sa
from config.enums.role import RoleEnum


def create_users_table():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(50), unique=True, index=True),
        sa.Column("email", sa.String, unique=True, index=True),
        sa.Column("password", sa.String),
        sa.Column("image", sa.String),
        sa.Column(
            "role",
            sa.Enum(RoleEnum),
            index=True,
        ),
        sa.Column("address", sa.String),
        sa.Column("phone", sa.String, unique=True, index=True),
        sa.Column("profession", sa.String, index=True),
    )


def remove_users_table():
    op.drop_table("users") 
