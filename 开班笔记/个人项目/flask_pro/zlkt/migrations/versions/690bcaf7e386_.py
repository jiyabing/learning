"""empty message

Revision ID: 690bcaf7e386
Revises: 1d9e07faae6a
Create Date: 2018-09-03 19:15:41.575374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '690bcaf7e386'
down_revision = '1d9e07faae6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'create_time')
    # ### end Alembic commands ###
