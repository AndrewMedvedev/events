from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from .database.models import EventModel, NewsModel, VisitorModel


class EventResponse(BaseModel):
    id: int
    created_at: datetime
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

    def to_model(self) -> EventModel:
        return EventModel(
            name_event=self.name_event,
            date_time=self.date_time,
            location=self.location,
            description=self.description,
            limit_people=self.limit_people,
            points_for_the_event=self.points_for_the_event,
        )


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


class NewsSchema(BaseModel):
    title: str
    body: str
    image: str | None = None

    def to_model(self) -> NewsModel:
        return NewsModel(title=self.title, body=self.body, image=self.image)


class VisitorSchema(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: str
    event_id: int
    unique_string: str

    @classmethod
    def create(cls, visitor: dict) -> VisitorSchema:
        return cls(
            user_id=visitor["user_id"],
            first_name=visitor["first_name"],
            last_name=visitor["last_name"],
            email=visitor["email"],
            event_id=visitor["event_id"],
            unique_string=f"{uuid.uuid4()!s}{uuid.uuid4()!s}",
        )

    def to_model(self) -> VisitorModel:
        return VisitorModel(
            user_id=self.user_id,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            event_id=self.event_id,
            unique_string=self.unique_string,
        )


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
