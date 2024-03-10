from abc import ABC

from services.data_provider_service.news_provider_base import NewsProviderBase
from services.data_provider_service.note_provider_base import NoteProviderBase
from services.data_provider_service.sticker_provider_base import StickerProviderBase
from services.data_provider_service.user_provider_base import UserProviderBase


class DataProviderBase(UserProviderBase, StickerProviderBase, NoteProviderBase, NewsProviderBase, ABC):
    pass
