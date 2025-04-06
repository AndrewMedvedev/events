from typing import List

from datetime import datetime

from pydantic import BaseModel


class EventResponse(BaseModel):
    id: int
    name_event: str
    date_time: datetime
    location: str
    description: str
    limit_people: int | None
    points_for_the_event: int | None

    class Config:
        from_attributes = True


class EventListResponse(BaseModel):
    events: List[EventResponse]
