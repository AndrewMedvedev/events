from typing import Optional

import contextlib
from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config import get_db_url


class DatabaseSessionService:
    def __init__(self) -> None:
        self._engine: Optional[AsyncEngine] = None
        self._sessionmaker: Optional[async_sessionmaker[AsyncSession]] = None

    def init(self) -> None:
        self._engine = create_async_engine(url=get_db_url(), echo=True)
        self._sessionmaker = async_sessionmaker(bind=self._engine, expire_on_commit=False)

    async def close(self) -> None:
        if self._engine is None:
            return
        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def session(self):
        async with self._sessionmaker() as session:
            try:
                yield session
            except Exception as exc:
                await session.rollback()
                raise exc

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise OSError("DatabaseSessionManager is not initialized")
        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception as exc:
                await connection.rollback()
                raise exc


db_session = DatabaseSessionService()


async def get_session():
    async with db_session.session() as session:
        yield session
