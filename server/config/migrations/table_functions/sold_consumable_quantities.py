import sqlalchemy as sa
from alembic import op
from datetime import datetime


def create_sold_consumable_quantities_table():
    op.create_table(
        "sold_consumable_quantities",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("consumable_id", sa.Integer, nullable=False, index=True),
        sa.Column("farmer_id", sa.Integer, nullable=False, index=True),
        sa.Column("quantity_sold", sa.Float, nullable=False, index=True),
        sa.Column("date_sold", sa.DateTime, nullable=False, index=True),
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
        sa.ForeignKeyConstraint(["consumable_id"], ["consumables.id"]),
        sa.ForeignKeyConstraint(["farmer_id"], ["users.id"]),
    )


def remove_sold_consumable_quantities_table():
    op.drop_table("sold_consumable_quantities")
