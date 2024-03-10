import uvicorn
from fastapi import FastAPI

from controllers import sticker_controller, user_controller, news_controller, note_controller

app = FastAPI()
app.include_router(sticker_controller.router)
app.include_router(user_controller.router)
app.include_router(news_controller.router)
app.include_router(note_controller.router)


if __name__ == "__main__":
    uvicorn.run(app, ws="websockets", host="0.0.0.0", port=24110, http="h11")
    # poetry run uvicorn --ws websockets --port 24110 main:app --reload
