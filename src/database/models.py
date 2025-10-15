from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import (
    Base,
    FloatNotNull,
    IntNull,
    StrNotNull,
    StrNullable,
    StrUniq,
    UUIDNotNull,
)


class NewsModel(Base):
    __tablename__ = "news"
    __table_args__ = ({"extend_existing": True},)

    title: Mapped[StrNotNull]
    body: Mapped[StrNotNull]
    image: Mapped[StrNullable]


class EventModel(Base):
    __tablename__ = "events"
    __table_args__ = ({"extend_existing": True},)

    name_event: Mapped[StrUniq]
    date_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    location: Mapped[StrNotNull]
    description: Mapped[StrNotNull]
    limit_people: Mapped[IntNull]
    points_for_the_event: Mapped[FloatNotNull]
    visitors: Mapped[list[VisitorModel]] = relationship(
        "VisitorModel",
        back_populates="event",
        cascade="all, delete-orphan",
    )


class VisitorModel(Base):
    __tablename__ = "visitors"

    user_id: Mapped[UUIDNotNull]
    event_id: Mapped[int] = mapped_column(ForeignKey(EventModel.id))
    first_name: Mapped[StrNotNull]
    last_name: Mapped[StrNotNull]
    email: Mapped[StrNotNull]
    unique_string: Mapped[StrNotNull]
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

    user_id: Mapped[UUIDNotNull]
    points: Mapped[FloatNotNull]
