from pydantic import BaseModel
from datetime import datetime


class EventModel(BaseModel):
    name_event: str
    date_time: datetime
    location: str
    description: str
    limit_people: int | None


class EventModelUpdate(BaseModel):
    date_time: datetime | None
    location: str | None
    description: str | None
    limit_people: int | None


