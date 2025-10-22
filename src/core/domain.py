from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .utils import current_datetime


class EventSchema(BaseModel):
    id: int | None = None
    name_event: str
    date_time: datetime
    location: str
    description: str
    points_for_the_event: float = 0
    limit_people: int = 0
    created_at: datetime = Field(default_factory=current_datetime)

    model_config = ConfigDict(from_attributes=True)


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
    id: int | None = None
    title: str
    body: str
    image: str | None = None

    model_config = ConfigDict(from_attributes=True)


class VisitorSchema(BaseModel):
    id: int | None = None
    user_id: UUID
    first_name: str
    last_name: str
    email: str
    event_id: int
    unique_string: str = f"{uuid4()!s}{uuid4()!s}"
    created_at: datetime = Field(default_factory=current_datetime)

    model_config = ConfigDict(from_attributes=True)


class UserSchema(BaseModel):
    event_id: int
    unique_string: str

    model_config = ConfigDict(from_attributes=True)
