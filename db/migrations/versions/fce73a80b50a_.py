"""empty message

Revision ID: fce73a80b50a
Revises: 12abbd32e0d2
Create Date: 2024-03-04 13:30:12.423416

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fce73a80b50a'
down_revision: Union[str, None] = '12abbd32e0d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_check_constraint(
        "check_user_login_length",
        "tbl_User",
        sa.text("LENGTH(login) > 2")
    )
    op.create_check_constraint(
        "check_user_password_length",
        "tbl_User",
        sa.text("LENGTH(password) > 8")
    )
    op.create_check_constraint(
        "check_user_firstname_length",
        "tbl_User",
        sa.text("LENGTH(firstname) > 2")
    )
    op.create_check_constraint(
        "check_user_lastname_length",
        "tbl_User",
        sa.text("LENGTH(lastname) > 2")
    )
    op.create_check_constraint(
        "check_news_title_length",
        "tbl_News",
        sa.text("LENGTH(title) > 2")
    )
    op.create_check_constraint(
        "check_news_content_length",
        "tbl_News",
        sa.text("LENGTH(content) > 4")
    )
    op.create_check_constraint(
        "check_note_content_length",
        "tbl_Note",
        sa.text("LENGTH(content) > 2")
    )
    op.create_check_constraint(
        "check_sticker_name_length",
        "tbl_Sticker",
        sa.text("LENGTH(name) > 2")
    )
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
