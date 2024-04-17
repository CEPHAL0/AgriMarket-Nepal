from alembic import op
import sqlalchemy as sa
from config.enums import consumable
from datetime import datetime


def create_consumables_table():
    op.create_table(
        "consumables",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String, nullable=False, index=True),
        sa.Column(
            "type", sa.Enum(consumable.ConsumableEnum), nullable=False, index=True
        ),
        sa.Column("image_path", sa.String, nullable=False, index=True),
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


def remove_consumables_table():
    op.drop_table("consumables")
    op.execute("DROP TYPE IF EXISTS consumableenum")
