from abc import ABC, abstractmethod

from schemas.schemas import StickerAddSchema, StickerUpdateSchema


class StickerProviderBase(ABC):

    @abstractmethod
    def create_sticker(self, item: StickerAddSchema):
        """Создание нового стикера"""

    @abstractmethod
    def get_stickers(self):
        """Получение всех стикеров"""

    @abstractmethod
    def get_sticker(self, id):
        """Получение стикера по id"""

    @abstractmethod
    def delete_sticker(self, item_id):
        """Удаление стикера по id"""

    @abstractmethod
    def update_sticker(self, item: StickerUpdateSchema):
        """Обновление стикера"""
