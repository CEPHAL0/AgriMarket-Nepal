from alembic import op
import sqlalchemy as sa


def create_districs_table():
    op.create_table(
        "districts",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String, index=True),
        sa.Column("province_id", sa.Integer, nullable=False),
        sa.Column("ecological_region", sa.String, index=True),
        sa.ForeignKeyConstraint(["province_id"], ["provinces.id"]),
    )


def remove_districts_table():
    op.drop_table("districts")
