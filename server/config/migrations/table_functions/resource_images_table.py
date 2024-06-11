from alembic import op
import sqlalchemy as sa
from datetime import datetime


def create_resource_images_table():
    op.create_table(
        "resource_images",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("resource_id", sa.Integer, nullable=False, index=True),
        sa.Column("image_path", sa.String, nullable=False, index=True),
        sa.Column("order", sa.Integer, nullable=False, index=True),
        sa.ForeignKeyConstraint(
            ["resource_id"],
            ["resources.id"],
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


def remove_resource_images_table():
    op.drop_table("resource_images")
