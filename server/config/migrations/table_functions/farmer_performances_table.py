from alembic import op
import sqlalchemy as sa
from datetime import datetime


def create_farmer_performances_table():
    op.create_table(
        "farmer_performances",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("farmer_id", sa.Integer, nullable=False, index=True),
        sa.Column("performance", sa.Float, nullable=False, index=True),
        sa.ForeignKeyConstraint(
            ["farmer_id"],
            ["users.id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
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


def remove_farmer_performances_table():
    op.drop_table("farmer_performances")
