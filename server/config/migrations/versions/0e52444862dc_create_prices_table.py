"""Create Prices Table

Revision ID: 0e52444862dc
Revises: 731ef75184e5
Create Date: 2024-04-15 21:19:39.327897

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from config.migrations.table_functions import index


# revision identifiers, used by Alembic.
revision: str = "0e52444862dc"
down_revision: Union[str, None] = "731ef75184e5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.prices_table.create_prices_table()


def downgrade() -> None:
    index.prices_table.remove_prices_table()
