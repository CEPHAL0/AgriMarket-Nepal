"""Create Resources Table

Revision ID: 73e2770470af
Revises: 50a96ec920f5
Create Date: 2024-04-15 21:34:16.018959

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from config.migrations.table_functions import index


# revision identifiers, used by Alembic.
revision: str = "73e2770470af"
down_revision: Union[str, None] = "50a96ec920f5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.resources_table.create_resources_table()


def downgrade() -> None:
    index.resources_table.remove_resources_table()
