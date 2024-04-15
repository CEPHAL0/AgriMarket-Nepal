from alembic import op
import sqlalchemy as sa
from config.enums.role import RoleEnum
from datetime import datetime


def create_provinces_table():
    op.create_table(
        "provinces",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String, nullable=False, index=True),
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


def remove_provinces_table():
    op.drop_table("provinces")
