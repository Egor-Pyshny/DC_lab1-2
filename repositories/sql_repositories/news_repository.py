from sqlalchemy import select, delete

from models.NewsStickerModel import News
from repositories.repository_base import RepositoryBase
from repositories.sql_repositories import Session, with_session


class SQLNewsRepository(RepositoryBase):

    def create(self, item: News):
        with Session() as session:
            with session.begin():
                session.add(item)
        return item

    @with_session
    def get_all(self, session):
        query = select(News)
        res = session.execute(query)
        res_orm = res.scalars().all()
        return res_orm

    @with_session
    def get(self, session, id):
        query = select(News).where(News.id == id)
        res = session.execute(query)
        res_orm = res.scalars().all()
        return res_orm

    @with_session
    def delete(self, session, item_id):
        query = delete(News).where(News.id == item_id)
        res = session.execute(query)
        return res.rowcount

    @with_session
    def update(self, session, item: News):
        news = session.query(News).get(item.id)
        if item.title is not None:
            news.title = item.title
        if item.content is not None:
            news.content = item.content
        if item.userid is not None:
            news.userid = item.userid
        if item.created is not None:
            news.created = item.created
        if item.modified is not None:
            news.modified = item.modified
        return news
