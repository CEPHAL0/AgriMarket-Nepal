"""Create Districts Table

Revision ID: 5fdccfcd3283
Revises: 0177cae329a7
Create Date: 2024-04-15 16:04:46.366763

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from config.migrations.table_functions import index


# revision identifiers, used by Alembic.
revision: str = "5fdccfcd3283"
down_revision: Union[str, None] = "0177cae329a7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.districts_table.create_districs_table()


def downgrade() -> None:
    index.districts_table.remove_districts_table()
