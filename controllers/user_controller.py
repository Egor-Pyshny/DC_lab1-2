from typing import List
from fastapi.responses import Response
from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError, DataError
from starlette import status

from controllers import catch_check_error, dbcore
from schemas.schemas import UserUpdateSchema, UserSchema, UserAddSchema

router = APIRouter(
    prefix="/api/v1.0/users",
    tags=["users"],
)


@router.post("", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserAddSchema):
    try:
        return dbcore.create_user(user)
    except (IntegrityError, DataError) as e:
        return catch_check_error(e)


@router.get("", response_model=List[UserSchema], status_code=status.HTTP_200_OK)
def get_users():
    return dbcore.get_users()


@router.get("/{item_id}", response_model=UserSchema, status_code=status.HTTP_200_OK)
def get_user(item_id):
    return dbcore.get_user(item_id)


@router.delete("/{item_id}")
def delete_user(item_id):
    if dbcore.delete_user(item_id) == 0:
        return Response(status_code=400)
    else:
        return Response(status_code=204)


@router.put("", status_code=status.HTTP_200_OK)
def update_user(item: UserUpdateSchema):
    try:
        return dbcore.update_user(item)
    except IntegrityError as e:
        return catch_check_error(e)
