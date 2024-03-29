"""empty message

Revision ID: ad7dcac8bb54
Revises: 838f987d90f4
Create Date: 2021-04-23 21:17:15.103450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad7dcac8bb54'
down_revision = '838f987d90f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_users')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=255, collation='NOCASE'), nullable=False))
        batch_op.drop_constraint('uq_users_email', type_='unique')
        batch_op.create_unique_constraint(batch_op.f('uq_users_username'), ['username'])
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=255), nullable=False))
        batch_op.drop_constraint(batch_op.f('uq_users_username'), type_='unique')
        batch_op.create_unique_constraint('uq_users_email', ['email'])
        batch_op.drop_column('username')

    op.create_table('_alembic_tmp_users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text("'1'"), nullable=False),
    sa.Column('password', sa.VARCHAR(length=255), server_default=sa.text("('')"), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=100), server_default=sa.text("('')"), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=100), server_default=sa.text("('')"), nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_users'),
    sa.UniqueConstraint('username', name='uq_users_username')
    )
    # ### end Alembic commands ###
