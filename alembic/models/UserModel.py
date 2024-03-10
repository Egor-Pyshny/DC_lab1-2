from models import Base
from sqlalchemy import (
    CheckConstraint,
    Column,
    BIGINT,
    String,
)


class User(Base):
    __tablename__ = "tbl_User"

    id = Column(
        BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
    )
    login = Column(
        String(64),
        nullable=False,
        unique=True,
    )
    login_length_constraint = CheckConstraint("LENGTH(login) > 2", name="check_user_login_length")
    password = Column(
        String(128),
        CheckConstraint("length(password) >= 8", name="check_user_password_field_length"),
        nullable=False,
    )
    firstname = Column(
        String(64),
        CheckConstraint("length(firstname) >= 2", name="check_user_firstname_field_length"),
        nullable=False,
    )
    lastname = Column(
        String(64),
        CheckConstraint("length(lastname) >= 2", name="check_user_lastname_field_length"),
        nullable=False,
    )
