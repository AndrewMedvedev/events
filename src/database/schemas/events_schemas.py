from datetime import datetime

from pydantic import BaseModel


class EventModel(BaseModel):
    name_event: str
    date_time: datetime
    location: str
    description: str
    points_for_the_event: int | None
    limit_people: int | None


class EventModelUpdate(BaseModel):
    date_time: datetime | None
    location: str | None
    description: str | None
    limit_people: int | None


