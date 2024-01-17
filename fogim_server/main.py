import uvicorn
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/media", StaticFiles(directory="media"), name="media")


@app.get("/")
def get_root():
    return "Fellowship Of Grace International Ministries (FOGIM)"


def start():
    uvicorn.run("fogim_server.main:app", host="0.0.0.0", port=8000, reload=True)
