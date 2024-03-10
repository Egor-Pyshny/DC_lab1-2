from typing import List
from fastapi.responses import Response
from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError, DataError
from starlette import status

from controllers import catch_check_error, dbcore
from schemas.schemas import NewsSchema, NewsUpdateSchema, NewsAddSchema

router = APIRouter(
    prefix="/api/v1.0/news",
    tags=["news"],
)


@router.post("", response_model=NewsSchema, status_code=status.HTTP_201_CREATED)
def create_news(news: NewsAddSchema):
    try:
        return dbcore.create_news(news)
    except (IntegrityError, DataError) as e:
        return catch_check_error(e)


@router.get("", response_model=List[NewsSchema], status_code=status.HTTP_200_OK)
def get_news():
    return dbcore.get_news()


@router.get("/{item_id}", response_model=NewsSchema, status_code=status.HTTP_200_OK)
def get_new(item_id):
    return dbcore.get_new(item_id)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_new(item_id):
    if dbcore.delete_news(item_id) == 0:
        return Response(status_code=400)
    else:
        return Response(status_code=204)


@router.put("", status_code=status.HTTP_200_OK)
def update_new(item: NewsUpdateSchema):
    try:
        return dbcore.update_news(item)
    except IntegrityError as e:
        return catch_check_error(e)
