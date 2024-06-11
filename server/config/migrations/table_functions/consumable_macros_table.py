from alembic import op
import sqlalchemy as sa
from datetime import datetime


def create_consumable_macros_table():
    op.create_table(
        "consumable_macros",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("consumable_id", sa.Integer, nullable=False, index=True),
        sa.Column("macro_type_id", sa.Integer, nullable=False, index=True),
        sa.Column("quantity", sa.Float, nullable=False, index=True),
        sa.ForeignKeyConstraint(
            ["consumable_id"],
            ["consumables.id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["macro_type_id"],
            ["macro_types.id"],
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


def remove_consumable_macros_table():
    op.drop_table("consumable_macros")
