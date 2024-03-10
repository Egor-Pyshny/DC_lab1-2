from sqlalchemy.orm import relationship

from models import Base
from sqlalchemy import (
    CheckConstraint,
    Column,
    BIGINT,
    String,
    ForeignKey,
    DateTime,
    Table,
)


news_sticker_association = Table(
    "tbl_NewsSticker",
    Base.metadata,
    Column(
        "news_sticker_association_id",
        BIGINT,
        autoincrement=True,
        nullable=False,
        unique=True,
        primary_key=True,
    ),
    Column(
        "news_id",
        BIGINT,
        ForeignKey(
            "tbl_News.id", ondelete="CASCADE"),
    ),
    Column(
        "sticker_id",
        BIGINT,
        ForeignKey("tbl_Sticker.id", ondelete="CASCADE"),
    ),
)


class Sticker(Base):
    __tablename__ = "tbl_Sticker"

    id = Column(
        BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
    )
    name = Column(
        String(32),
        CheckConstraint("length(login) >= 2", name="check_sticker_name_field_length"),
        nullable=False,
        unique=True,
    )
    news = relationship(
        "News",
        secondary=news_sticker_association,
        back_populates="sticker",
        passive_deletes=True,
    )


class News(Base):
    __tablename__ = "tbl_News"

    id = Column(
        BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
    )
    userid = Column(
        BIGINT,
        ForeignKey('tbl_User.id'),
        nullable=False,
    )
    title = Column(
        String(64),
        CheckConstraint("length(title) >= 2", name="check_news_title_field_length"),
        nullable=False,
        unique=True,
    )
    content = Column(
        String(2048),
        CheckConstraint("length(content) >= 4", name="check_news_content_field_length"),
    )
    created = Column(
        DateTime,
        nullable=False,
    )
    modified = Column(
        DateTime,
        nullable=False,
    )
    sticker = relationship(
        "Sticker",
        secondary=news_sticker_association,
        back_populates="news",
        passive_deletes=True,
    )
