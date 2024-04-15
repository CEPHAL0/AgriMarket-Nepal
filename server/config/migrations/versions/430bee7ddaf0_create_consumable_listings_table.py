"""Create Consumable Listings Table

Revision ID: 430bee7ddaf0
Revises: 7bc540d9c691
Create Date: 2024-04-15 16:31:54.986522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '430bee7ddaf0'
down_revision: Union[str, None] = '7bc540d9c691'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
