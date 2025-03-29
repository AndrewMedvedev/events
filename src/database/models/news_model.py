from src.database.database import (
    Base,
    int_pk,
    created_at,
    str_nullable,
)

from sqlalchemy.orm import Mapped


class New(Base):

    __table_args__ = {"extend_existing": True}

    id: Mapped[int_pk]
    created_at: Mapped[created_at]
    body: Mapped[str_nullable]
    image: Mapped[str_nullable]

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})"
        )

    def __repr__(self):
        return str(self)
