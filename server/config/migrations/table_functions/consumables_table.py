from alembic import op
import sqlalchemy as sa
from config.enums import consumable


def create_consumables_table():
    op.create_table(
        "consumables",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String, index=True),
        sa.Column("type", sa.Enum(consumable.ConsumableEnum), index=True),
        sa.Column("image_path", sa.String, index=True),
    )


def remove_consumables_table():
    op.drop_table("consumables")
