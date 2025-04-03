from sqlalchemy.orm import Mapped

from src.database.database import Base, created_at, int_pk, str_nullable


class New(Base):

    __table_args__ = {"extend_existing": True}

    id: Mapped[int_pk]
    created_at: Mapped[created_at]
    title: Mapped[str_nullable]
    body: Mapped[str_nullable]
    image: Mapped[str_nullable]

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"created_at={self.created_at!r},"
            f"title={self.title!r},"
            f"body={self.body!r},"
            f"image={self.image!r},"
        )

    def __repr__(self):
        return str(self)
