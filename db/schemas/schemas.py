from pydantic import BaseModel, ConfigDict
from datetime import datetime


class NewsAddSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    userid: int
    title: str
    content: str


class NewsSchema(NewsAddSchema):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    news_id: int | None = None
    created: datetime
    modified: datetime


class NewsUpdateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int
    userid: int | None = None
    title: str | None = None
    content: str | None = None
    id: int | None = None
    created: datetime | None = None
    updated: datetime | None = None


class UserAddSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    login: str
    password: str
    firstname: str
    lastname: str


class UserSchema(UserAddSchema):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int | None = None


class UserUpdateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int
    login: str | None = None
    password: str | None = None
    firstname: str | None = None
    lastname: str | None = None


class NoteAddSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    newsid: int
    content: str


class NoteSchema(NoteAddSchema):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int | None = None


class NoteUpdateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    note_id: int
    newsid: int | None = None
    content: str | None = None


class StickerAddSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    name: str


class StickerSchema(StickerAddSchema):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int | None = None


class StickerUpdateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int
    name: str | None = None
