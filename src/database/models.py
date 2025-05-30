from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import (
    Base,
    created_at,
    float_nullable,
    int_null_true,
    int_pk,
    str_null_true,
    str_nullable,
    str_uniq,
    uuid_nullable,
)


class NewsModel(Base):
    __tablename__ = "news"
    __table_args__ = ({"extend_existing": True},)

    id: Mapped[int_pk]
    created_at: Mapped[created_at]
    title: Mapped[str_nullable]
    body: Mapped[str_nullable]
    image: Mapped[str_null_true]


class EventModel(Base):
    __tablename__ = "events"
    __table_args__ = ({"extend_existing": True},)

    id: Mapped[int_pk]
    created_at: Mapped[created_at]
    name_event: Mapped[str_uniq]
    date_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    location: Mapped[str_nullable]
    description: Mapped[str_nullable]
    limit_people: Mapped[int_null_true]
    points_for_the_event: Mapped[float_nullable]
    visitors: Mapped[list[VisitorModel]] = relationship(
        "VisitorModel",
        back_populates="event",
        cascade="all, delete-orphan",
    )


class VisitorModel(Base):
    __tablename__ = "visitors"

    id: Mapped[int_pk]
    created_at: Mapped[created_at]
    user_id: Mapped[uuid_nullable]
    event_id: Mapped[int] = mapped_column(ForeignKey(EventModel.id))
    first_name: Mapped[str_nullable]
    last_name: Mapped[str_nullable]
    email: Mapped[str_nullable]
    unique_string: Mapped[str_nullable]
    event: Mapped[list[EventModel]] = relationship(
        "EventModel",
        back_populates="visitors",
    )

    __table_args__ = (
        UniqueConstraint("user_id", "event_id", "first_name", "last_name", "email"),
        {"extend_existing": True},
    )


class PointsModel(Base):
    __tablename__ = "points"

    id: Mapped[int_pk]
    user_id: Mapped[uuid_nullable]
    points: Mapped[float_nullable]
