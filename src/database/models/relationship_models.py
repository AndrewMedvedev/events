from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import (
    Base,
    int_null_true,
    int_nullable,
    int_pk,
    str_nullable,
    str_uniq,
)


class Event(Base):

    __table_args__ = {"extend_existing": True}

    id: Mapped[int_pk]
    name_event: Mapped[str_uniq]
    date_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    location: Mapped[str_nullable]
    description: Mapped[str_nullable]
    limit_people: Mapped[int_null_true]
    points_for_the_event: Mapped[int_null_true]
    visitors: Mapped[list["Visitor"]] = relationship(
        "Visitor",
        back_populates="event",
        cascade="all, delete-orphan",
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})"
        )

    def __repr__(self):
        return str(self)


class Visitor(Base):

    id: Mapped[int_pk]
    user_id: Mapped[int_nullable]
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    first_name: Mapped[str_nullable]
    last_name: Mapped[str_nullable]
    email: Mapped[str_nullable]
    unique_string: Mapped[str_nullable]
    event: Mapped[list["Event"]] = relationship(
        "Event",
        back_populates="visitors",
    )

    __table_args__ = (
        UniqueConstraint("user_id", "event_id", "first_name", "last_name", "email"),
        {"extend_existing": True},
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})"
        )

    def __repr__(self):
        return str(self)
