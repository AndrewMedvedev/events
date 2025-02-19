from sqlalchemy.orm import Mapped

from src.database.database import (
    Base,
    int_pk,
    int_null_true,
    str_uniq,
    str_nullable,
    str_null_true,
)


class Event(Base):
    id: Mapped[int_pk]
    name_event: Mapped[str_nullable]
    date: Mapped[str_nullable]
    time: Mapped[str_nullable]
    location: Mapped[str_nullable]
    limit_people: Mapped[int_null_true]

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})"
        )

    def __repr__(self):
        return str(self)
