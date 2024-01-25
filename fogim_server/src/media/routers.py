import time
from datetime import datetime
from fastapi import APIRouter, UploadFile
from .models import Media

router = APIRouter()


@router.post("/media", response_model=Media)
async def create_file(files: list[UploadFile]):
    for file in files:
        # Generate a unique filename and create the media object
        fileName = (
            file.filename.split(".")[0]
            + "_"
            + str(round(time.time() * 1000))
            + "."
            + file.filename.split(".")[-1]
        )
        object_name = (
            "inteliport_media/top_10_holding/"
            + str(datetime.now().date())
            + "/"
            + fileName
        )
