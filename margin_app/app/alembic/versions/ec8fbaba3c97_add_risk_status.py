"""Add risk status

Revision ID: ec8fbaba3c97
Revises: d23e53e374ba
Create Date: 2025-02-22 21:24:04.598637

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ec8fbaba3c97'
down_revision: Union[str, None] = 'd23e53e374ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add risk_status enum to pool"""
    # ### commands auto generated by Alembic - please adjust! ###
    sa.Enum('low', 'medium', 'high', name='pool_risk_status').create(op.get_bind())
    with op.batch_alter_table('pool', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'risk_status', 
                postgresql.ENUM(
                    'low', 'medium', 'high', name='pool_risk_status', 
                    create_type=False
                ), nullable=False
            )
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    """Drop risk_status enum from pool"""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pool', schema=None) as batch_op:
        batch_op.drop_column('risk_status')

    sa.Enum('low', 'medium', 'high', name='pool_risk_status').drop(op.get_bind())
    # ### end Alembic commands ###
