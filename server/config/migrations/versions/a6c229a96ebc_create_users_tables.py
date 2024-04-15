"""Create User Table

Revision ID: a6c229a96ebc
Revises: 
Create Date: 2024-04-14 22:17:02.316320

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from config.enums.role import RoleEnum
from config.migrations.table_functions import index


# revision identifiers, used by Alembic.
revision: str = "a6c229a96ebc"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.users_table.create_users_table()


def downgrade() -> None:
    index.users_table.remove_users_table()
