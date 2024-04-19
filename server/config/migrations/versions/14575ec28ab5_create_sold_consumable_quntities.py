"""Create Sold Consumable Quntities

Revision ID: 14575ec28ab5
Revises: 6cc9f3cfbeb6
Create Date: 2024-04-19 10:29:44.234413

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from config.migrations.table_functions import index


# revision identifiers, used by Alembic.
revision: str = "14575ec28ab5"
down_revision: Union[str, None] = "6cc9f3cfbeb6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.sold_consumable_quantities.create_sold_consumable_quantities_table()


def downgrade() -> None:
    index.sold_consumable_quantities.remove_sold_consumable_quantities_table()
