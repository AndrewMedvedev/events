
from pydantic import BaseModel


class NewsModel(BaseModel):
    body: str
    image: str