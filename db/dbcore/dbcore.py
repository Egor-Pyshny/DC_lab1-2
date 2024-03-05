import datetime

from sqlalchemy import select, delete

from dbcore import Session
from db.models.NewsStickerModel import News, Sticker
from db.models.NoteModel import Note
from db.models.UserModel import User
from db.schemas.schemas import *
from db.dbcore.data_provider_base import DataProvider


def with_session(func):
    def wrapper(self, *args, **kwargs):
        with Session() as session:
            with session.begin():
                res = func(self, session, *args, **kwargs)
        return res
    return wrapper


class SQLProvider(DataProvider):

    def create_news(self, item: NewsAddSchema):
        with Session() as session:
            with session.begin():
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

    def create_user(self, item: UserAddSchema):
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

    def create_note(self, item: NoteAddSchema):
        with Session() as session:
            with session.begin():
                res = Note(
                    newsid=item.newsid,
                    content=item.content,
                )
                session.add(res)
            result_dto = NoteSchema.model_validate(res)
        return result_dto

    def create_sticker(self, item: StickerAddSchema):
        with Session() as session:
            with session.begin():
                res = Sticker(
                    name=item.name,
                )
                session.add(res)
            result_dto = StickerSchema.model_validate(res)
        return result_dto

    @with_session
    def get_news(self, session):
        query = select(News)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [NewsSchema.model_validate(row) for row in res_orm]
        return result_dtos

    @with_session
    def get_users(self, session):
        query = select(User)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [UserSchema.model_validate(row) for row in res_orm]
        return result_dtos

    @with_session
    def get_stickers(self, session):
        query = select(Sticker)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [StickerSchema.model_validate(row) for row in res_orm]
        return result_dtos

    @with_session
    def get_notes(self, session):
        query = select(Note)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [NoteSchema.model_validate(row) for row in res_orm]
        return result_dtos

    @with_session
    def get_new(self, session, id):
        query = select(News).where(News.id == id)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [NewsSchema.model_validate(row) for row in res_orm]
        return result_dtos[0]

    @with_session
    def get_user(self, session, id):
        query = select(User).where(User.id == id)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [UserSchema.model_validate(row) for row in res_orm]
        return result_dtos[0]

    @with_session
    def get_sticker(self, session, id):
        query = select(Sticker).where(Sticker.id == id)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [StickerSchema.model_validate(row) for row in res_orm]
        return result_dtos[0]

    @with_session
    def get_note(self, session, id):
        query = select(Note).where(Note.id == id)
        res = session.execute(query)
        res_orm = res.scalars().all()
        result_dtos = [NoteSchema.model_validate(row) for row in res_orm]
        return result_dtos[0]

    @with_session
    def delete_news(self, session, item_id):
        query = delete(News).where(News.id == item_id)
        res = session.execute(query)
        return res.rowcount

    @with_session
    def delete_user(self, session, item_id):
        query = delete(User).where(User.id == item_id)
        res = session.execute(query)
        return res.rowcount

    @with_session
    def delete_sticker(self, session, item_id):
        query = delete(Sticker).where(Sticker.id == item_id)
        res = session.execute(query)
        return res.rowcount

    @with_session
    def delete_note(self, session, item_id):
        query = delete(Note).where(Note.id == item_id)
        res = session.execute(query)
        return res.rowcount

    @with_session
    def update_news(self, session, item: NewsUpdateSchema):
        news = session.query(News).get(item.id)
        if item.title is not None:
            news.title = item.title
        if item.content is not None:
            news.content = item.content
        if item.userid is not None:
            news.userid = item.userid
        if item.created is not None:
            news.created = item.created
        if item.updated is not None:
            news.modified = item.updated
        return NewsSchema.from_orm(news)

    @with_session
    def update_user(self, session, item: UserUpdateSchema):
        user = session.query(User).get(item.id)
        if item.login is not None:
            user.login = item.login
        if item.password is not None:
            user.password = item.password
        if item.firstname is not None:
            user.firstname = item.firstname
        if item.lastname is not None:
            user.lastname = item.lastname
        return UserSchema.from_orm(user)

    @with_session
    def update_sticker(self, session, item: StickerUpdateSchema):
        sticker = session.query(Sticker).get(item.id)
        if item.name is not None:
            sticker.name = item.name
        return StickerSchema.from_orm(sticker)

    @with_session
    def update_note(self, session, item: NoteUpdateSchema):
        note = session.query(Note).get(item.id)
        if item.newsid is not None:
            note.newsid = item.newsid
        if item.content is not None:
            note.content = item.content
        return NoteSchema.from_orm(note)
