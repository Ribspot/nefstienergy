"""empty message

Revision ID: ec28cc765ec4
Revises: ea15428b4ec1
Create Date: 2023-07-24 18:12:46.074602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec28cc765ec4'
down_revision = 'ea15428b4ec1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service',
    sa.Column('service_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('service_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('service_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    # ### end Alembic commands ###
