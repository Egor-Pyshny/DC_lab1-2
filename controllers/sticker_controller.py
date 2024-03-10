from typing import List
from fastapi.responses import Response
from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError, DataError
from starlette import status

from controllers import catch_check_error, dbcore
from schemas.schemas import StickerSchema, StickerAddSchema, StickerUpdateSchema

router = APIRouter(
    prefix="/api/v1.0/stickers",
    tags=["stickers"],
)


@router.post("", response_model=StickerSchema, status_code=status.HTTP_201_CREATED)
def create_sticker(sticker: StickerAddSchema):
    try:
        return dbcore.create_sticker(sticker)
    except (IntegrityError, DataError) as e:
        return catch_check_error(e)


@router.get("", response_model=List[StickerSchema], status_code=status.HTTP_200_OK)
def get_stickers():
    return dbcore.get_stickers()


@router.get("/{item_id}", response_model=StickerSchema, status_code=status.HTTP_200_OK)
def get_sticker(item_id):
    return dbcore.get_sticker(item_id)


@router.put("", status_code=status.HTTP_200_OK)
def update_sticker(item: StickerUpdateSchema):
    try:
        return dbcore.update_sticker(item)
    except IntegrityError as e:
        return catch_check_error(e)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sticker(item_id):
    if dbcore.delete_sticker(item_id) == 0:
        return Response(status_code=400)
    else:
        return Response(status_code=204)
