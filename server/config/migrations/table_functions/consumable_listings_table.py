from alembic import op
import sqlalchemy as sa
from datetime import datetime


def create_consumable_listings_table():
    op.create_table(
        "consumable_listings",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("consumable_id", sa.Integer, nullable=False),
        sa.Column("user_id", sa.Integer, nullable=False),
        sa.Column("district_id", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(
            ["consumable_id"],
            ["consumables.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["district_id"],
            ["districts.id"],
        ),
        sa.Column("posted_date", sa.DateTime, nullable=False),
        sa.Column("expiry_date", sa.DateTime, nullable=False),
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


def remove_consumable_listings_table():
    op.drop_table("consumable_listings")
