from alembic import op
import sqlalchemy as sa
from datetime import datetime


def create_districs_table():
    op.create_table(
        "districts",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String, nullable=False, index=True),
        sa.Column("province_id", sa.Integer, nullable=False),
        sa.Column("ecological_region", sa.String, nullable=False, index=True),
        sa.ForeignKeyConstraint(
            ["province_id"],
            ["provinces.id"],
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


def remove_districts_table():
    op.drop_table("districts")
