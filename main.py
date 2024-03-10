import json
from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response
from sqlalchemy.exc import IntegrityError, DataError
from starlette import status

from schemas.schemas import *
from services.data_provider_service.data_provider import DataProvider

app = FastAPI()
dbcore = DataProvider()


def catch_check_error(e):
    hash_code = abs(hash(e.args[0]))
    first_two_digits = str(hash_code)[:2]
    resp_status = 400
    if isinstance(e, IntegrityError):
        if "UniqueViolation" in e.args[0]:
            resp_status = 403
    res = {"errorMessage": f"{e.args[0]}", "errorCode": f"{resp_status}{first_two_digits}"}
    return Response(status_code=resp_status, content=json.dumps(res))


@app.post("/api/v1.0/news", response_model=NewsSchema, status_code=status.HTTP_201_CREATED)
def create_news(news: NewsAddSchema):
    try:
        return dbcore.create_news(news)
    except (IntegrityError, DataError) as e:
        return catch_check_error(e)


@app.post("/api/v1.0/users", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserAddSchema):
    try:
        return dbcore.create_user(user)
    except (IntegrityError, DataError) as e:
        return catch_check_error(e)


@app.post("/api/v1.0/stickers", response_model=StickerSchema, status_code=status.HTTP_201_CREATED)
def create_sticker(sticker: StickerAddSchema):
    try:
        return dbcore.create_sticker(sticker)
    except (IntegrityError, DataError) as e:
        return catch_check_error(e)


@app.post("/api/v1.0/notes", response_model=NoteSchema, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteAddSchema):
    try:
        return dbcore.create_note(note)
    except (IntegrityError, DataError) as e:
        return catch_check_error(e)


@app.get("/api/v1.0/news", response_model=List[NewsSchema], status_code=status.HTTP_200_OK)
def get_news():
    return dbcore.get_news()


@app.get("/api/v1.0/users", response_model=List[UserSchema], status_code=status.HTTP_200_OK)
def get_users():
    return dbcore.get_users()


@app.get("/api/v1.0/stickers", response_model=List[StickerSchema], status_code=status.HTTP_200_OK)
def get_stickers():
    return dbcore.get_stickers()


@app.get("/api/v1.0/notes", response_model=List[NoteSchema], status_code=status.HTTP_200_OK)
def get_notes():
    return dbcore.get_notes()


@app.get("/api/v1.0/news/{item_id}", response_model=NewsSchema, status_code=status.HTTP_200_OK)
def get_new(item_id):
    return dbcore.get_new(item_id)


@app.get("/api/v1.0/users/{item_id}", response_model=UserSchema, status_code=status.HTTP_200_OK)
def get_user(item_id):
    return dbcore.get_user(item_id)


@app.get("/api/v1.0/stickers/{item_id}", response_model=StickerSchema, status_code=status.HTTP_200_OK)
def get_sticker(item_id):
    return dbcore.get_sticker(item_id)


@app.get("/api/v1.0/notes/{item_id}", response_model=NoteSchema, status_code=status.HTTP_200_OK)
def get_note(item_id):
    return dbcore.get_note(item_id)


@app.delete("/api/v1.0/news/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_new(item_id):
    if dbcore.delete_news(item_id) == 0:
        return Response(status_code=400)
    else:
        return Response(status_code=204)


@app.delete("/api/v1.0/users/{item_id}")
def delete_user(item_id):
    if dbcore.delete_user(item_id) == 0:
        return Response(status_code=400)
    else:
        return Response(status_code=204)


@app.delete("/api/v1.0/stickers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sticker(item_id):
    if dbcore.delete_sticker(item_id) == 0:
        return Response(status_code=400)
    else:
        return Response(status_code=204)


@app.delete("/api/v1.0/notes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(item_id):
    if dbcore.delete_note(item_id) == 0:
        return Response(status_code=400)
    else:
        return Response(status_code=204)


@app.put("/api/v1.0/news", status_code=status.HTTP_200_OK)
def update_new(item: NewsUpdateSchema):
    try:
        return dbcore.update_news(item)
    except IntegrityError as e:
        return catch_check_error(e)


@app.put("/api/v1.0/users", status_code=status.HTTP_200_OK)
def update_user(item: UserUpdateSchema):
    try:
        return dbcore.update_user(item)
    except IntegrityError as e:
        return catch_check_error(e)


@app.put("/api/v1.0/stickers", status_code=status.HTTP_200_OK)
def update_sticker(item: StickerUpdateSchema):
    try:
        return dbcore.update_sticker(item)
    except IntegrityError as e:
        return catch_check_error(e)


@app.put("/api/v1.0/notes", status_code=status.HTTP_200_OK)
def update_note(item: NoteUpdateSchema):
    try:
        return dbcore.update_note(item)
    except IntegrityError as e:
        return catch_check_error(e)


if __name__ == "__main__":
    uvicorn.run(app, ws="websockets", host="0.0.0.0", port=24110, http="h11")
    # poetry run uvicorn --ws websockets  --port 24110 main:app --reload
