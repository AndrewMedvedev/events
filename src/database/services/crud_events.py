import logging

from sqlalchemy import select

from src.database.models import Event
from src.database.schemas import EventListResponse
from src.errors import DataBaseError
from src.interfaces import CRUDEventBase

from .orm import DatabaseSessionService

log = logging.getLogger(__name__)


class CRUDEvents(DatabaseSessionService, CRUDEventBase):

    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_event(
        self,
        model: Event,
    ) -> dict:
        async with self.session() as session:
            try:
                session.add(model)
                await session.commit()
                await session.refresh(model)
                return "done"
            except Exception:
                raise DataBaseError(
                    detail="create_event",
                )

    async def read_event(self) -> EventListResponse:
        async with self.session() as session:
            events = await session.execute(select(Event))
        try:
            return EventListResponse(events=events.scalars().all())

        except Exception:
            raise DataBaseError(
                detail="read_event",
            )

    async def read_events_with_limit(
        self,
        page: int = 1,
        limit: int = 5,
    ) -> EventListResponse:
        offset = (page - 1) * limit
        async with self.session() as session:
            stmt = select(Event).offset(offset).limit(limit)
            events = await session.execute(stmt)
        return EventListResponse(events=events.scalars().all())

    async def delete_event(
        self,
        model_id: int,
    ) -> dict:
        async with self.session() as session:
            obj = await session.get(Event, model_id)
            try:
                if obj:
                    await session.delete(obj)
                    await session.commit()
                    return "done"
                raise DataBaseError(
                    detail="delete_event",
                )
            except Exception:
                raise DataBaseError(
                    detail="delete_event",
                )
