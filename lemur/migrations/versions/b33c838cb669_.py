"""adding index on the not_after field

Revision ID: b33c838cb669
Revises: 318b66568358
Create Date: 2019-05-30 08:42:05.294109

"""

# revision identifiers, used by Alembic.
revision = 'b33c838cb669'
down_revision = '318b66568358'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_certificates_not_after', 'certificates', [sa.text('not_after DESC')], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_certificates_not_after', table_name='certificates')
    # ### end Alembic commands ###