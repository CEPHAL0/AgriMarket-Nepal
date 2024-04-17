"""Create Consumables Table

Revision ID: 7bc540d9c691
Revises: 5fdccfcd3283
Create Date: 2024-04-15 16:12:37.428431

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from config.migrations.table_functions import index


# revision identifiers, used by Alembic.
revision: str = "7bc540d9c691"
down_revision: Union[str, None] = "5fdccfcd3283"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.consumables_table.create_consumables_table()


def downgrade() -> None:
    index.consumables_table.remove_consumables_table()
