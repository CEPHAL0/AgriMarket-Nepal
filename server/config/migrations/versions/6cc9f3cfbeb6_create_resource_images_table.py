"""Create Resource Images Table

Revision ID: 6cc9f3cfbeb6
Revises: 73e2770470af
Create Date: 2024-04-15 21:38:31.484135

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from config.migrations.table_functions import index


# revision identifiers, used by Alembic.
revision: str = "6cc9f3cfbeb6"
down_revision: Union[str, None] = "73e2770470af"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    index.resource_images_table.create_resource_images_table()


def downgrade() -> None:
    index.resource_images_table.remove_resource_images_table()
