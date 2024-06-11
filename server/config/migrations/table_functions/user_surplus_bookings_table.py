from alembic import op
import sqlalchemy as sa
from datetime import datetime
from config.enums.accepted import AcceptedEnum


def create_user_surplus_bookings_table():
    op.create_table(
        "user_surplus_bookings",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, index=True),
        sa.Column("surplus_listing_id", sa.Integer, nullable=False, index=True),
        sa.Column("booker_id", sa.Integer, nullable=False, index=True),
        sa.ForeignKeyConstraint(
            ["booker_id"],
            ["users.id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["surplus_listing_id"],
            ["surplus_listings.id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.Column("accepted", sa.Enum(AcceptedEnum), nullable=False, index=True),
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
    op.execute("DROP TYPE IF EXISTS acceptedenum")
