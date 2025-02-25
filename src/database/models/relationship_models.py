from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import (
    Base,
    int_nullable,
    int_pk,
    datetime,
    str_null_true,
    str_nullable,
    str_uniq,
)


class Event(Base):

    __table_args__ = {"extend_existing": True}

    id: Mapped[int_pk]
    name_event: Mapped[str_uniq]
    date: Mapped[datetime]
    time: Mapped[str_nullable]
    location: Mapped[str_nullable]
    description: Mapped[str_nullable]
    limit_people: Mapped[str_null_true]
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

    __table_args__ = {"extend_existing": True}

    id: Mapped[int_pk]
    user_id: Mapped[int_nullable]
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    first_name: Mapped[str_nullable]
    last_name: Mapped[str_nullable]
    email: Mapped[str_nullable]
    event: Mapped[list["Event"]] = relationship(
        "Event",
        back_populates="visitors",
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})"
        )

    def __repr__(self):
        return str(self)
