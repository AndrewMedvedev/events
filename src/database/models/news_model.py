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
        return f"{self.__class__.__name__}(id={self.id}, created_at={self.created_at!r},title={self.title!r},body={self.body!r},image={self.image!r},"

    def __repr__(self):
        return str(self)
