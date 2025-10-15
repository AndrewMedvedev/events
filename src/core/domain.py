from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, field_validator


class EventResponse(BaseModel):
    id: int
    created_at: datetime
    name_event: str
    date_time: datetime
    location: str
    description: str
    limit_people: int | None
    points_for_the_event: float | None

    model_config = ConfigDict(from_attributes=True)

    @field_validator("date_time")
    def valid_datetime(cls, v):
        return v.isoformat()


class EventSchema(BaseModel):
    name_event: str
    date_time: datetime
    location: str
    description: str
    points_for_the_event: float | None = None
    limit_people: int | None = None


class NewsResponse(BaseModel):
    id: int
    title: str
    body: str
    image: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

    @field_validator("created_at")
    def valid_datetime(cls, v):
        return v.isoformat()


class NewsSchema(BaseModel):
    title: str
    body: str
    image: str | None = None


class VisitorSchema(BaseModel):
    user_id: UUID
    first_name: str
    last_name: str
    email: str
    event_id: int
    unique_string: str = f"{uuid4()!s}{uuid4()!s}"


class UserSchema(BaseModel):
    event_id: int
    unique_string: str
