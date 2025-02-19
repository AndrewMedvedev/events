from pydantic import BaseModel


class EventModel(BaseModel):
    name_event: str
    date: str
    time: str
    location: str
    limit_people: int | None