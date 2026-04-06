from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create tables
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False, unique=True)
    )
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(length=100), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('jobs')
