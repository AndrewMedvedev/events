from typing import Annotated

from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, func
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

StrNotNull = Annotated[str, mapped_column(nullable=False)]
StrNullable = Annotated[str | None, mapped_column(nullable=True)]
IntPK = Annotated[int, mapped_column(primary_key=True)]
FloatNotNull = Annotated[float, mapped_column(nullable=False)]
UUIDNotNull = Annotated[UUID, mapped_column(nullable=False)]
IntNotNull = Annotated[int, mapped_column(nullable=False)]
StrUniq = Annotated[str, mapped_column(unique=True, nullable=False)]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[IntPK]

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


def create_sessionmaker(sqlalchemy_url: str) -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(url=sqlalchemy_url, echo=True)
    return async_sessionmaker(engine, class_=AsyncSession, autoflush=False, expire_on_commit=False)
