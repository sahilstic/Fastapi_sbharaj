"""add content to posts table

Revision ID: ba33eb4d1a6e
Revises: 6c46c8cde009
Create Date: 2024-04-05 21:02:13.470093

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba33eb4d1a6e'
down_revision: Union[str, None] = '6c46c8cde009'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
