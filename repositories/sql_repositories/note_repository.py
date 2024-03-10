from sqlalchemy import select, delete

from models.NoteModel import Note
from repositories.repository_base import RepositoryBase
from repositories.sql_repositories import with_session, Session


class SQLNoteRepository(RepositoryBase):

    def create(self, item: Note):
        with Session() as session:
            with session.begin():
                session.add(item)
        return item

    @with_session
    def get_all(self, session):
        query = select(Note)
        res = session.execute(query)
        res_orm = res.scalars().all()
        return res_orm

    @with_session
    def get(self, session, id):
        query = select(Note).where(Note.id == id)
        res = session.execute(query)
        res_orm = res.scalars().all()
        return res_orm

    @with_session
    def delete(self, session, item_id):
        query = delete(Note).where(Note.id == item_id)
        res = session.execute(query)
        return res.rowcount

    def update(self, item: Note):
        with Session() as session:
            with session.begin():
                note = session.query(Note).get(item.id)
                if item.newsid is not None:
                    note.newsid = item.newsid
                if item.content is not None:
                    note.content = item.content
        return note
