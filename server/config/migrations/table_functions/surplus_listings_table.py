from alembic import op
import sqlalchemy as sa
from config.enums import booked
from datetime import datetime


def create_surplus_listings_table():
    op.create_table(
        "surplus_listings",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("consumable_id", sa.Integer, nullable=False, index=True),
        sa.Column("price", sa.Float, nullable=False, index=True),
        sa.Column("booked", sa.Enum(booked.BookedEnum), nullable=False, index=True),
        sa.ForeignKeyConstraint(["consumable_id"], ["consumables.id"]),
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


def remove_surplus_listings_table():
    op.drop_table("surplus_listings")
    op.execute("DROP TYPE IF EXISTS bookedenum")
