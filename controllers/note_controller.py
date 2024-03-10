from typing import List
from fastapi.responses import Response
from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError, DataError
from starlette import status

from controllers import catch_check_error, dbcore
from schemas.schemas import NoteUpdateSchema, NoteSchema, NoteAddSchema

router = APIRouter(
    prefix="/api/v1.0/notes",
    tags=["news"],
)


@router.post("", response_model=NoteSchema, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteAddSchema):
    try:
        return dbcore.create_note(note)
    except (IntegrityError, DataError) as e:
        return catch_check_error(e)


@router.get("", response_model=List[NoteSchema], status_code=status.HTTP_200_OK)
def get_notes():
    return dbcore.get_notes()


@router.get("/{item_id}", response_model=NoteSchema, status_code=status.HTTP_200_OK)
def get_note(item_id):
    return dbcore.get_note(item_id)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(item_id):
    if dbcore.delete_note(item_id) == 0:
        return Response(status_code=400)
    else:
        return Response(status_code=204)


@router.put("", status_code=status.HTTP_200_OK)
def update_note(item: NoteUpdateSchema):
    try:
        return dbcore.update_note(item)
    except IntegrityError as e:
        return catch_check_error(e)
