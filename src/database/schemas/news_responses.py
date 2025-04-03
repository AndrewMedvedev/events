from datetime import datetime
from typing import List

from pydantic import BaseModel


class NewsResponse(BaseModel):
    id: int
    created_at: datetime
    title: str
    body: str
    image: str

    class Config:
        from_attributes = True


class NewsListResponse(BaseModel):
    news: List[NewsResponse]
