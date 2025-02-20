from pydantic import BaseModel


class EventModel(BaseModel):
    name_event: str
    date: str
    time: str
    location: str
    limit_people: str | None


class EventModelUpdate(BaseModel):
    date: str | None
    time: str | None
    location: str | None
    limit_people: str | None