from datetime import datetime
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.ext.asyncio import (AsyncAttrs, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column

from src.config import get_db_url

DATABASE_URL = get_db_url()


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

created_at = Annotated[datetime, mapped_column(server_default=func.now())]
int_pk = Annotated[int, mapped_column(primary_key=True)]
int_nullable = Annotated[int, mapped_column(nullable=False)]
int_null_true = Annotated[int, mapped_column(nullable=True)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_nullable = Annotated[str, mapped_column(nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
