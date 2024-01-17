"""Create user table

Revision ID: 107d6fb75724
Revises: f7868c99f9ca
Create Date: 2024-01-17 15:24:53.835536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '107d6fb75724'
down_revision = 'f7868c99f9ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('email', sa.String(length=500), nullable=False),
    sa.Column('password', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
