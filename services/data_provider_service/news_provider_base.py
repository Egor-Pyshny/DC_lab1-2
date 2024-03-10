from abc import ABC, abstractmethod

from schemas.schemas import NewsAddSchema, NewsUpdateSchema


class NewsProviderBase(ABC):

    @abstractmethod
    def create_news(self, item: NewsAddSchema):
        """Создание новой новости"""


    @abstractmethod
    def get_news(self):
        """Получение всех новостей"""


    @abstractmethod
    def get_new(self, id):
        """Получение новости по id"""


    @abstractmethod
    def delete_news(self, item_id):
        """Удаление новости по id"""


    @abstractmethod
    def update_news(self, item: NewsUpdateSchema):
        """Обновление новости"""
