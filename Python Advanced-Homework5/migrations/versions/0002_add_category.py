# migrations/versions/0002_add_category.py
from alembic import op
import sqlalchemy as sa

revision = "0002_add_category"
down_revision = "0001_initial"
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.add_column("questions", sa.Column("category_id", sa.Integer(), nullable=True))
    op.create_index("ix_questions_category_id", "questions", ["category_id"], unique=False)
    op.create_foreign_key(
        "fk_questions_category_id",
        "questions",
        "categories",
        ["category_id"],
        ["id"],
        ondelete="SET NULL",
    )

def downgrade():
    op.drop_constraint("fk_questions_category_id", "questions", type_="foreignkey")
    op.drop_index("ix_questions_category_id", table_name="questions")
    op.drop_column("questions", "category_id")
    op.drop_table("categories")
