from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator

from src.database.models import VisitorModel


class EventGetParams(BaseModel):
    is_paginated: bool
    page: int
    limit: int

    def to_dict(self) -> dict:
        return {
            "is_paginated": str(self.is_paginated),
            "page": self.page,
            "limit": self.limit,
        }


class EventResponse(BaseModel):
    id: int
    name_event: str
    date_time: datetime
    location: str
    description: str
    limit_people: int | None
    points_for_the_event: int | None

    model_config = ConfigDict(from_attributes=True)

    def to_dict(self) -> dict:
        result = {
            "id": self.id,
            "name_event": self.name_event,
            "date_time": self.date_time.isoformat(),
            "location": self.location,
            "description": self.description,
        }
        if self.limit_people is not None:
            result["limit_people"] = self.limit_people
        if self.points_for_the_event is not None:
            result["points_for_the_event"] = self.points_for_the_event

        return result


class EventListResponse(BaseModel):
    events: list[EventResponse]

    def to_dict(self) -> dict:
        return {"event": [e.to_dict() for e in self.events]}


class EventSchema(BaseModel):
    name_event: str
    date_time: datetime
    location: str
    description: str
    points_for_the_event: int | None = None
    limit_people: int | None = None

    @field_validator("date_time")
    def valid_datetime(cls, v):
        return v.isoformat()

    def to_dict(self) -> dict:
        return {
            "name_event": self.name_event,
            "date_time": self.date_time,
            "location": self.location,
            "description": self.description,
            "limit_people": self.limit_people,
            "points_for_the_event": self.points_for_the_event,
        }


class NewsGetParams(BaseModel):
    is_paginated: bool
    page: int
    limit: int

    def to_dict(self) -> dict:
        return {
            "is_paginated": str(self.is_paginated),
            "page": self.page,
            "limit": self.limit,
        }


class NewsAddTest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    title: str
    body: str
    image: bytes | None = None

    def to_dict(self) -> dict:
        if self.image is None:
            return {
                "data": {
                    "title": self.title,
                    "body": self.body,
                },
            }
        return {
            "data": {
                "title": self.title,
                "body": self.body,
            },
            "files": {"image": ("test.jpg", self.image, "image/jpeg")},
        }


class NewsResponse(BaseModel):
    id: int
    title: str
    body: str
    image: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "image": self.image,
            "created_at": self.created_at.isoformat(),
        }


class NewsListResponse(BaseModel):
    news: list[NewsResponse]

    def to_dict(self) -> dict:
        return {"news": [n.to_dict() for n in self.news]}


class UserSchema(BaseModel):
    event_id: int
    unique_string: str

    @classmethod
    def from_model(cls, user: VisitorModel) -> UserSchema:
        return cls(event_id=user.event_id, unique_string=user.unique_string)

    def to_dict(self) -> dict:
        return {"event_id": self.event_id, "unique_string": self.unique_string}


class UserEventSchema(BaseModel):
    user_event: list[UserSchema]

    @classmethod
    def create(cls, event: list) -> UserEventSchema:
        return cls(user_event=[UserSchema.from_model(u) for u in event])

    def to_dict(self) -> dict:
        return {"user_event": [u.to_dict() for u in self.user_event]}
