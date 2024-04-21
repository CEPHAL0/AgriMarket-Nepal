from alembic import op
import sqlalchemy as sa
from datetime import datetime


def create_prices_table():
    op.create_table(
        "prices",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column("consumable_id", sa.Integer, nullable=False, index=True),
        sa.Column("price", sa.Float, nullable=False, index=True),
        sa.ForeignKeyConstraint(["consumable_id"], ["consumables.id"]),
        sa.Column("date", sa.DateTime, nullable=False, index=True),
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


def remove_prices_table():
    op.drop_table("prices")
