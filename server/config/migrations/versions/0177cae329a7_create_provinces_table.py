"""Create Provinces Table

Revision ID: 0177cae329a7
Revises: a6c229a96ebc
Create Date: 2024-04-15 14:01:20.888798

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from config.migrations.table_functions import index


# revision identifiers, used by Alembic.
revision: str = "0177cae329a7"
down_revision: Union[str, None] = "a6c229a96ebc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.provinces_table.create_provinces_table()


def downgrade() -> None:
    index.provinces_table.remove_provinces_table()
