"""Create Phone Number for user column

Revision ID: 5a3286b0dd98
Revises: 
Create Date: 2026-07-26 10:58:33.534224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a3286b0dd98'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # pass
    op.add_column('users', sa.Column('phone_number', sa.String(length=15), nullable=True))





def downgrade() -> None:
    """Downgrade schema."""
    # pass
    op.drop_column('users', 'phone_number')
