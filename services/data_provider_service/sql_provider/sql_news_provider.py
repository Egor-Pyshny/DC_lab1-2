from datetime import datetime

from alembic.models.NewsStickerModel import News
from repositories.sql_repositories.news_repository import SQLNewsRepository
from schemas.schemas import NewsAddSchema, NewsUpdateSchema, NewsSchema
from services.data_provider_service.news_provider_base import NewsProviderBase


class NewsProvider(NewsProviderBase):

    def __init__(self):
        self.repository = SQLNewsRepository()

    def create_news(self, item: NewsAddSchema):
        res = News(
                    userId=item.userid,
                    title=item.title,
                    content=item.content,
                    created=datetime.now(),
                    modified=datetime.now(),
                )
        news_orm = self.repository.create(res)
        return NewsSchema.model_validate(news_orm)

    def get_news(self):
        news_orm = self.repository.get_all()
        result_dtos = [NewsSchema.model_validate(row) for row in news_orm]
        return result_dtos

    def get_new(self, id):
        news_orm = self.repository.get(id)
        result_dtos = [NewsSchema.model_validate(row) for row in news_orm]
        return result_dtos[0]

    def delete_news(self, item_id):
        return self.repository.delete(item_id)

    def update_news(self, item: NewsUpdateSchema):
        res = News(
                    id=item.id,
                    userId=item.userid,
                    title=item.title,
                    content=item.content,
                    created=datetime.now(),
                    modified=datetime.now(),
                )
        news_orm = self.repository.update(res)
        return NewsSchema.model_validate(news_orm)
