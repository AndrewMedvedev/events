from sqlalchemy.orm import Mapped

from src.database.database import (
    Base,
    int_nullable,
    int_pk,
)


class PointsEvent(Base):
    id: Mapped[int_pk]
    user_id: Mapped[int_nullable]
    points: Mapped[int_nullable]

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})"
        )

    def __repr__(self):
        return str(self)
