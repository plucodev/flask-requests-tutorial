"""empty message

Revision ID: 35b22e87f5f4
Revises: bbf91365387c
Create Date: 2019-08-21 20:21:47.823021

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '35b22e87f5f4'
down_revision = 'bbf91365387c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=120), nullable=True))
    op.drop_column('user', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', mysql.VARCHAR(length=120), nullable=True))
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###