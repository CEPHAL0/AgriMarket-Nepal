from alembic import op
import sqlalchemy as sa
from datetime import datetime


def create_macro_types_table():
    op.create_table(
        "macro_types",
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


def remove_macro_types_table():
    op.drop_table("macro_types")
