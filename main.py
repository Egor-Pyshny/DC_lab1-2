import json
from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response
from sqlalchemy.exc import IntegrityError
from starlette import status

from db.dbcore.dbcore import dbcore
from db.schemas.schemas import *

app = FastAPI()


@app.post("/api/v1.0/news", response_model=NewsSchema, status_code=status.HTTP_201_CREATED)
def create_news(news: NewsAddSchema):
    return dbcore.create_news(news)


@app.post("/api/v1.0/users", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserAddSchema):
    return dbcore.create_user(user)


@app.post("/api/v1.0/stickers", response_model=StickerSchema, status_code=status.HTTP_201_CREATED)
def create_sticker(sticker: StickerAddSchema):
    return dbcore.create_sticker(sticker)


@app.post("/api/v1.0/notes", response_model=NoteSchema, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteAddSchema):
    return dbcore.create_note(note)


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
        res = {"errorMessage": f"{e.args[0]}", "errorCode": 40022}
        return Response(status_code=400, content=json.dumps(res))


@app.put("/api/v1.0/users", status_code=status.HTTP_200_OK)
def update_user(item: UserUpdateSchema):
    try:
        return dbcore.update_user(item)
    except IntegrityError as e:
        res = {"errorMessage": f"{e.args[0]}", "errorCode": 40022}
        return Response(status_code=400, content=json.dumps(res))


@app.put("/api/v1.0/stickers", status_code=status.HTTP_200_OK)
def update_sticker(item: StickerUpdateSchema):
    try:
        return dbcore.update_sticker(item)
    except IntegrityError as e:
        res = {"errorMessage": f"{e.args[0]}", "errorCode": 40022}
        return Response(status_code=400, content=json.dumps(res))


@app.put("/api/v1.0/notes", status_code=status.HTTP_200_OK)
def update_note(item: NoteUpdateSchema):
    try:
        return dbcore.update_note(item)
    except IntegrityError as e:
        res = {"errorMessage": f"{e.args[0]}", "errorCode": 40022}
        return Response(status_code=400, content=json.dumps(res))

# @app.patch("/items/{item_id}", response_model=Item)
# def update_item(item_id: str, item: Item):
#     stored_item_data = items[item_id]
#     stored_item_model = Item(**stored_item_data)
#     update_data = item.dict(exclude_unset=True)
#     updated_item = stored_item_model.copy(update=update_data)
#     items[item_id] = jsonable_encoder(updated_item)
#     return updated_item


if __name__ == "__main__":
    uvicorn.run(app, ws="websockets", host="0.0.0.0", port=24110, http="h11")
    # poetry run uvicorn --ws websockets  --port 24110 main:app --reload
