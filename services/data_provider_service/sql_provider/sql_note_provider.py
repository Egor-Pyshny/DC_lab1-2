from alembic.models.NoteModel import Note
from repositories.sql_repositories.note_repository import SQLNoteRepository
from schemas.schemas import NoteUpdateSchema, NoteAddSchema, NoteSchema
from services.data_provider_service.note_provider_base import NoteProviderBase


class NoteProvider(NoteProviderBase):

    def __init__(self):
        self.repository = SQLNoteRepository()

    def create_note(self, item: NoteAddSchema):
        res = Note(
                    newsId=item.newsid,
                    content=item.content,
                )
        note_orm = self.repository.create(res)
        return NoteSchema.model_validate(note_orm)

    def get_notes(self):
        note_orm = self.repository.get_all()
        result_dtos = [NoteSchema.model_validate(row) for row in note_orm]
        return result_dtos

    def get_note(self, id):
        note_orm = self.repository.get(id)
        result_dtos = [NoteSchema.model_validate(row) for row in note_orm]
        return result_dtos[0]

    def delete_note(self, item_id):
        return self.repository.delete(item_id)

    def update_note(self, item: NoteUpdateSchema):
        res = Note(
                    id=item.id,
                    newsId=item.newsid,
                    content=item.content,
                )
        note_orm = self.repository.update(res)
        return NoteSchema.model_validate(note_orm)
