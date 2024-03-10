from schemas.schemas import *
from services.data_provider_service.data_provider_base import DataProviderBase
from services.data_provider_service.sql_provider.sql_news_provider import NewsProvider
from services.data_provider_service.sql_provider.sql_note_provider import NoteProvider
from services.data_provider_service.sql_provider.sql_sticker_provider import StickerProvider
from services.data_provider_service.sql_provider.sql_user_provider import UserProvider


class DataProvider(DataProviderBase):

    def __init__(self):
        self.user_provider = UserProvider()
        self.news_provider = NewsProvider()
        self.note_provider = NoteProvider()
        self.sticker_provider = StickerProvider()

    def create_news(self, item: NewsAddSchema):
        return self.news_provider.create_news(item)

    def create_user(self, item: UserAddSchema):
        return self.user_provider.create_user(item)

    def create_note(self, item: NoteAddSchema):
        return self.note_provider.create_note(item)

    def create_sticker(self, item: StickerAddSchema):
        return self.sticker_provider.create_sticker(item)

    def get_news(self):
        return self.news_provider.get_news()

    def get_users(self):
        return self.user_provider.get_users()

    def get_stickers(self):
        return self.sticker_provider.get_stickers()

    def get_notes(self):
        return self.note_provider.get_notes()

    def get_new(self, id):
        return self.news_provider.get_new(id)

    def get_user(self, id):
        return self.user_provider.get_user(id)

    def get_sticker(self, id):
        return self.sticker_provider.get_sticker(id)

    def get_note(self, id):
        return self.note_provider.get_note(id)

    def delete_news(self, id):
        return self.news_provider.delete_news(id)

    def delete_user(self, id):
        return self.user_provider.delete_user(id)

    def delete_sticker(self, id):
        return self.sticker_provider.delete_sticker(id)

    def delete_note(self, id):
        return self.note_provider.delete_note(id)

    def update_news(self, item: NewsUpdateSchema):
        return self.news_provider.update_news(item)

    def update_user(self, item: UserUpdateSchema):
        return self.user_provider.update_user(item)

    def update_sticker(self, item: StickerUpdateSchema):
        return self.sticker_provider.update_sticker(item)

    def update_note(self, item: NoteUpdateSchema):
        return self.note_provider.update_note(item)
