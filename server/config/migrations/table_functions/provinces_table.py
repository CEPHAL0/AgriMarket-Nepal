from alembic import op
import sqlalchemy as sa
from config.enums.role import RoleEnum


def create_provinces_table():
    op.create_table(
        "provinces",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String, index=True),
    )


def remove_provinces_table():
    op.drop_table("provinces")
