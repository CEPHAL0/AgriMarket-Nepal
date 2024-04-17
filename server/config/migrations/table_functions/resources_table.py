from alembic import op
import sqlalchemy as sa
from datetime import datetime
from config.enums import audience


def create_resources_table():
    op.create_table(
        "resources",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "audience", sa.Enum(audience.AudienceEnum), nullable=False, index=True
        ),
        sa.Column("title", sa.String, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=False),
        sa.Column("author_id", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(["author_id"], ["users.id"]),
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


def remove_resources_table():
    op.drop_table("resources")
    op.execute("DROP TYPE IF EXISTS audienceenum")
