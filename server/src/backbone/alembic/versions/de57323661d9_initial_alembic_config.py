"""initial alembic config

Revision ID: de57323661d9
Revises: 
Create Date: 2019-10-20 14:12:41.173562

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'de57323661d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clans',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(length=40), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('children',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('api_key', sa.String(length=37), nullable=True),
                    sa.Column('level', sa.Integer(), nullable=True),
                    sa.Column('xp', sa.Integer(), nullable=True),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('username', sa.String(length=100), nullable=False),
                    sa.Column('clan_id', sa.Integer(), nullable=True),
                    sa.Column('registration_id', sa.String(length=200), nullable=True),
                    sa.ForeignKeyConstraint(['clan_id'], ['clans.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('api_key')
                    )
    op.create_table('parents',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('admin', sa.Boolean(), nullable=False),
                    sa.Column('api_key', sa.String(length=37), nullable=True),
                    sa.Column('name', sa.String(length=1000), nullable=False),
                    sa.Column('email', sa.String(length=100), nullable=False),
                    sa.Column('password', sa.String(length=100), nullable=False),
                    sa.Column('cp_code', sa.String(length=37), nullable=True),
                    sa.Column('ch_code', sa.String(length=37), nullable=True),
                    sa.Column('clan_id', sa.Integer(), nullable=True),
                    sa.Column('registration_id', sa.String(length=200), nullable=True),
                    sa.Column('picture', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['clan_id'], ['clans.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('api_key'),
                    sa.UniqueConstraint('ch_code'),
                    sa.UniqueConstraint('cp_code'),
                    sa.UniqueConstraint('email')
                    )
    op.create_table('friendships',
                    sa.Column('friend_a_id', sa.Integer(), nullable=False),
                    sa.Column('friend_b_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['friend_a_id'], ['parents.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['friend_b_id'], ['parents.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('friend_a_id', 'friend_b_id')
                    )
    op.create_table('quests',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('title', sa.String(length=350), nullable=False),
                    sa.Column('description', sa.String(length=1000), nullable=False),
                    sa.Column('reward', sa.Integer(), nullable=False),
                    sa.Column('owner', sa.Integer(), nullable=True),
                    sa.Column('due', sa.TIMESTAMP(), nullable=False),
                    sa.Column('recurring', sa.Boolean(), nullable=False),
                    sa.Column('needs_verification', sa.Boolean(), nullable=False),
                    sa.ForeignKeyConstraint(['owner'], ['children.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('questCompletions',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('owner', sa.Integer(), nullable=True),
                    sa.Column('value', sa.TIMESTAMP(), nullable=False),
                    sa.Column('ts', sa.TIMESTAMP(), nullable=False),
                    sa.ForeignKeyConstraint(['owner'], ['quests.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('questTimes',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('owner', sa.Integer(), nullable=True),
                    sa.Column('value', sa.Float(), nullable=False),
                    sa.ForeignKeyConstraint(['owner'], ['quests.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('questVerifications',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('owner', sa.Integer(), nullable=True),
                    sa.Column('value', sa.TIMESTAMP(), nullable=False),
                    sa.Column('ts', sa.TIMESTAMP(), nullable=False),
                    sa.ForeignKeyConstraint(['owner'], ['quests.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questVerifications')
    op.drop_table('questTimes')
    op.drop_table('questCompletions')
    op.drop_table('quests')
    op.drop_table('friendships')
    op.drop_table('parents')
    op.drop_table('children')
    op.drop_table('clans')
    # ### end Alembic commands ###
