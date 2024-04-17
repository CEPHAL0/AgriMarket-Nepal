"""Create Farmer Performances Table

Revision ID: 50a96ec920f5
Revises: 1afe0c67c85f
Create Date: 2024-04-15 21:29:12.450342

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from config.migrations.table_functions import index


# revision identifiers, used by Alembic.
revision: str = "50a96ec920f5"
down_revision: Union[str, None] = "1afe0c67c85f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.farmer_performances_table.create_farmer_performances_table()


def downgrade() -> None:
    index.farmer_performances_table.remove_farmer_performances_table()
