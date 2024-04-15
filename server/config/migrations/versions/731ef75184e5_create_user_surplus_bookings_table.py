"""Create User Surplus Bookings Table

Revision ID: 731ef75184e5
Revises: 55bb3a16d33e
Create Date: 2024-04-15 21:08:47.027278

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from config.migrations.table_functions import index

# revision identifiers, used by Alembic.
revision: str = "731ef75184e5"
down_revision: Union[str, None] = "55bb3a16d33e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.user_surplus_bookings_table.create_user_surplus_bookings_table()


def downgrade() -> None:
    index.user_surplus_bookings_table.remove_user_surplus_bookings_table()
