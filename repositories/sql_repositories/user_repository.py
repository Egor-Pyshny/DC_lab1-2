from sqlalchemy import select, delete

from models.UserModel import User
from repositories.repository_base import RepositoryBase
from repositories.sql_repositories import Session, with_session
from schemas.schemas import UserSchema


class SQLUserRepository(RepositoryBase):

    @with_session
    def create(self, session, item: User):
        session.add(item)

    @with_session
    def get_all(self, session):
        query = select(User)
        res = session.execute(query)
        res_orm = res.scalars().all()
        return res_orm

    @with_session
    def get(self, session, id):
        query = select(User).where(User.id == id)
        res = session.execute(query)
        res_orm = res.scalars().all()
        return res_orm

    @with_session
    def delete(self, session, item_id):
        query = delete(User).where(User.id == item_id)
        res = session.execute(query)
        return res.rowcount

    @with_session
    def update(self, session, item: User):
        user = session.query(User).get(item.id)
        if item.login is not None:
            user.login = item.login
        if item.password is not None:
            user.password = item.password
        if item.firstname is not None:
            user.firstname = item.firstname
        if item.lastname is not None:
            user.lastname = item.lastname
        return item
