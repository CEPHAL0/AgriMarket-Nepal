"""Create Macro Types Table

Revision ID: 5839d639e373
Revises: 0e52444862dc
Create Date: 2024-04-15 21:21:58.998152

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from config.migrations.table_functions import index


# revision identifiers, used by Alembic.
revision: str = "5839d639e373"
down_revision: Union[str, None] = "0e52444862dc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.macro_types_table.create_macro_types_table()


def downgrade() -> None:
    index.macro_types_table.remove_macro_types_table()
