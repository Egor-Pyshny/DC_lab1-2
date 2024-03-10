from models.NewsStickerModel import Sticker
from repositories.sql_repositories.sticker_repository import SQLStickerRepository
from schemas.schemas import StickerUpdateSchema, StickerAddSchema, StickerSchema
from services.data_provider_service.sticker_provider_base import StickerProviderBase


class StickerProvider(StickerProviderBase):

    def __init__(self):
        self.repository = SQLStickerRepository()

    def create_sticker(self, item: StickerAddSchema):
        res = Sticker(
                    name=item.name,
                )
        sticker_orm = self.repository.create(res)
        return StickerSchema.model_validate(sticker_orm)

    def get_stickers(self):
        sticker_orm = self.repository.get_all()
        result_dtos = [StickerSchema.model_validate(row) for row in sticker_orm]
        return result_dtos

    def get_sticker(self, id):
        sticker_orm = self.repository.get(id)
        result_dtos = [StickerSchema.model_validate(row) for row in sticker_orm]
        return result_dtos[0]

    def delete_sticker(self, item_id):
        return self.repository.delete(item_id)

    def update_sticker(self, item: StickerUpdateSchema):
        res = Sticker(
            id=item.id,
            name=item.name,
        )
        sticker_orm = self.repository.update(res)
        return StickerSchema.model_validate(sticker_orm)
