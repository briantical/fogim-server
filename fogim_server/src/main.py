import uvicorn
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles
from .media.routers import router

app = FastAPI()

app.include_router(router)

app.mount("/media", StaticFiles(directory="media"), name="media")


@app.get("/")
def get_root():
    return "Fellowship Of Grace International Ministries (FOGIM)"


def start():
    uvicorn.run("fogim_server.src.main:app", host="0.0.0.0", port=8000, reload=True)
