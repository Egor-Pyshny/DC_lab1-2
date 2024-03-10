from sqlalchemy import select, delete

from alembic.models.NewsStickerModel import Sticker
from repositories.repository_base import RepositoryBase
from repositories.sql_repositories import Session, with_session


class SQLStickerRepository(RepositoryBase):

    def create(self, item: Sticker):
        with Session() as session:
            with session.begin():
                session.add(item)
        return item

    @with_session
    def get_all(self, session):
        query = select(Sticker)
        res = session.execute(query)
        res_orm = res.scalars().all()
        return res_orm

    @with_session
    def get(self, session, id):
        query = select(Sticker).where(Sticker.id == id)
        res = session.execute(query)
        res_orm = res.scalars().all()
        return res_orm

    @with_session
    def delete(self, session, item_id):
        query = delete(Sticker).where(Sticker.id == item_id)
        res = session.execute(query)
        return res.rowcount

    @with_session
    def update(self, session, item: Sticker):
        sticker = session.query(Sticker).get(item.id)
        if item.name is not None:
            sticker.name = item.name
        return sticker
