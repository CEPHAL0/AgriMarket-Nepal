"""Create Consumable Macros Table

Revision ID: 1afe0c67c85f
Revises: 5839d639e373
Create Date: 2024-04-15 21:25:20.515822

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from config.migrations.table_functions import index


# revision identifiers, used by Alembic.
revision: str = "1afe0c67c85f"
down_revision: Union[str, None] = "5839d639e373"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.consumable_macros_table.create_consumable_macros_table()


def downgrade() -> None:
    index.consumable_macros_table.remove_consumable_macros_table()
