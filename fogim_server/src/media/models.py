from pydantic import BaseModel
from pydantic import Field


class Media(BaseModel):
    name: str = Field(min_length=10)  # the modified file name
    path: str = Field(min_length=10)  # the stored path for the file
    type: str = Field(min_length=10)  # the type of file being stored; pdf,jpg,mp4
    description: str = Field(max_length=50)  # the description of file
