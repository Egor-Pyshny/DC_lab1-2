import datetime

from sqlalchemy import select, delete

from dbcore import Session
from db.models.NewsStickerModel import News, Sticker
from db.models.NoteModel import Note
from db.models.UserModel import User
from db.schemas.schemas import *


def with_session(func):
    def wrapper(*args, **kwargs):
        with Session() as session:
            with session.begin():
                res = func(session, *args, **kwargs)
        return res
    return wrapper


class dbcore:

    @staticmethod
    @with_session
    def create_news(session, item: NewsAddSchema):
        res = News(
            userid=item.userid,
            title=item.title,
            content=item.content,
            created=datetime.now(),
            modified=datetime.now(),
        )
        session.add(res)
        result_dto = NewsSchema.model_validate(res)
        return result_dto

    @staticmethod
    def create_user(item: UserAddSchema):
        with Session() as session:
            with session.begin():
                res = User(
                    login=item.login,
                    password=item.password,
                    firstname=item.firstname,
                    lastname=item.lastname,
                )
                session.add(res)
            result_dto = UserSchema.model_validate(res)
        return result_dto

    @staticmethod
    @with_session
    def create_note(session, item: NoteAddSchema):
        res = Note(
            newsid=item.newsid,
            content=item.content,
        )
        session.add(res)
        result_dto = NoteSchema.model_validate(res)
        return result_dto

    @staticmethod
    @with_session
    def create_sticker(session, item: StickerAddSchema):
        res = Sticker(
            name=item.name,
        )
        session.add(res)
        result_dto = StickerSchema.model_validate(res)
        return result_dto

    @staticmethod
    @with_session
    def get_news(session):
        query = select(News)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [NewsSchema.model_validate(row) for row in res_orm]
        return result_dtos

    @staticmethod
    @with_session
    def get_users(session):
        query = select(User)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [UserSchema.model_validate(row) for row in res_orm]
        return result_dtos

    @staticmethod
    @with_session
    def get_stickers(session):
        query = select(Sticker)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [StickerSchema.model_validate(row) for row in res_orm]
        return result_dtos

    @staticmethod
    @with_session
    def get_notes(session):
        query = select(Note)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [NoteSchema.model_validate(row) for row in res_orm]
        return result_dtos

    @staticmethod
    @with_session
    def get_new(session, id):
        query = select(News).where(News.id == id)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [NewsSchema.model_validate(row) for row in res_orm]
        return result_dtos

    @staticmethod
    @with_session
    def get_user(session, id):
        query = select(User).where(User.id == id)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [UserSchema.model_validate(row) for row in res_orm]
        return result_dtos[0]

    @staticmethod
    @with_session
    def get_sticker(session, id):
        query = select(Sticker).where(Sticker.id == id)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [StickerSchema.model_validate(row) for row in res_orm]
        return result_dtos

    @staticmethod
    @with_session
    def get_note(session, id):
        query = select(Note).where(Note.id == id)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [NoteSchema.model_validate(row) for row in res_orm]
        return result_dtos

    @staticmethod
    @with_session
    def delete_news(session, item_id):
        query = delete(News).where(News.id == item_id)
        res = session.execute(query)

    @staticmethod
    @with_session
    def delete_user(session, item_id):
        query = delete(User).where(User.id == item_id)
        res = session.execute(query)
        return res.rowcount

    @staticmethod
    @with_session
    def delete_sticker(session, item_id):
        query = delete(Sticker).where(Sticker.id == item_id)
        res = session.execute(query)

    @staticmethod
    @with_session
    def delete_note(session, item_id):
        query = delete(Note).where(Note.id == item_id)
        res = session.execute(query)

    @staticmethod
    @with_session
    def update_news(session, item: NewsUpdateSchema):
        news = session.query(Note).get(item.id)
        news.title = item.itle
        news.content = item.content
        news.userid = item.userid
        news.created = item.created
        news.modified = item.modified
        return NewsSchema.from_orm(news)

    @staticmethod
    @with_session
    def update_user(session, item: UserUpdateSchema):
        user = session.query(User).get(item.id)
        user.login = item.login
        user.password = item.password
        user.firstname = item.firstname
        user.lastname = item.lastname
        return UserSchema.from_orm(user)

    @staticmethod
    @with_session
    def update_sticker(session, item: StickerUpdateSchema):
        pass

    @staticmethod
    @with_session
    def update_note(session, item: NoteUpdateSchema):
        pass
