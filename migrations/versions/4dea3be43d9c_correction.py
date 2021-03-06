"""correction

Revision ID: 4dea3be43d9c
Revises: 2dfeeba38c9d
Create Date: 2022-05-19 06:12:08.782568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dea3be43d9c'
down_revision = '2dfeeba38c9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'userLoginAt',
               existing_type=sa.DATETIME(),
               nullable=False)
    op.drop_column('user', 'userDateOfBirth')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('userDateOfBirth', sa.DATE(), nullable=True))
    op.alter_column('user', 'userLoginAt',
               existing_type=sa.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###
