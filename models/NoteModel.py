from models import Base
from sqlalchemy import (
    CheckConstraint,
    Column,
    BIGINT,
    ForeignKey,
    String,
)


class Note(Base):
    __tablename__ = "tbl_Note"

    id = Column(
        BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
    )
    newsid = Column(
        BIGINT,
        ForeignKey('tbl_News.id'),
        nullable=False,
    )
    content = Column(
        String(2048),
        CheckConstraint("length(content) >= 2", name="check_note_content_field_length"),
    )
