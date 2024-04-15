"""Create Surplus Listings Table

Revision ID: 55bb3a16d33e
Revises: 430bee7ddaf0
Create Date: 2024-04-15 21:00:16.874319

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from config.migrations.table_functions import index


# revision identifiers, used by Alembic.
revision: str = "55bb3a16d33e"
down_revision: Union[str, None] = "430bee7ddaf0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.surplus_listings_table.create_surplus_listings_table()


def downgrade() -> None:
    index.surplus_listings_table.remove_surplus_listings_table()
