"""empty message

Revision ID: 0be6d79b6618
Revises: 
Create Date: 2022-08-06 19:04:27.917340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0be6d79b6618'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('etudiants', sa.Column('pays', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('etudiants', 'pays')
    # ### end Alembic commands ###
