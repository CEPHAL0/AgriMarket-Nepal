from alembic import op
import sqlalchemy as sa
from datetime import datetime


def create_user_surplus_bookings_table():
    op.create_table(
        "user_surplus_bookings",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, index=True),
        sa.Column("consumable_id", sa.Integer, nullable=False, index=True),
        sa.Column("poster_id", sa.Integer, nullable=False, index=True),
        sa.Column("booker_id", sa.Integer, nullable=False, index=True),
        sa.ForeignKeyConstraint(["poster_id"], ["users.id"]),
        sa.ForeignKeyConstraint(["booker_id"], ["users.id"]),
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


def remove_user_surplus_bookings_table():
    op.drop_table("user_surplus_bookings")
