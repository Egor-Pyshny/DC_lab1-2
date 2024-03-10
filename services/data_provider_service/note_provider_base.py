from abc import ABC, abstractmethod

from schemas.schemas import NoteAddSchema, NoteUpdateSchema


class NoteProviderBase(ABC):

    @abstractmethod
    def create_note(self, item: NoteAddSchema):
        """Создание новой пометки"""

    @abstractmethod
    def get_notes(self):
        """Получение всех пометок"""

    @abstractmethod
    def get_note(self, id):
        """Получение пометки по id"""

    @abstractmethod
    def delete_note(self, item_id):
        """Удаление пометки по id"""

    @abstractmethod
    def update_note(self, item: NoteUpdateSchema):
        """Обновление пометки"""
