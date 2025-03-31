from sqlalchemy import func, select

from src.database.models import Event, Visitor
from src.database.services.orm import DatabaseSessionService
from src.errors import DataBaseError
from src.interfaces import CRUDVisitorBase


class CRUDVisitors(DatabaseSessionService, CRUDVisitorBase):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_visitor(
        self,
        model: Visitor,
    ) -> dict:
        async with self.session() as session:
            try:
                counts = await session.scalar(
                    select(Event.limit_people).where(Event.id == model.event_id)
                )
                counts_visitors = await session.execute(
                    select(func.count())
                    .select_from(Visitor)
                    .filter(Visitor.event_id == model.event_id)
                )
                if counts_visitors.scalar() < counts or counts == 0:
                    session.add(model)
                    await session.commit()
                    await session.refresh(model)
                    return "done"
                else:
                    raise DataBaseError(
                        detail="create_visitor",
                    )
            except Exception:
                raise DataBaseError(
                        detail="create_visitor",
                    )

    async def get_visitors_events(
        self,
        user_id: int,
    ) -> dict | str:
        async with self.session() as session:
            data = await session.execute(
                select(Visitor).filter(Visitor.user_id == user_id)
            )
            try:
                return data.scalars().all()
            except Exception:
                raise DataBaseError(
                        detail="get_visitors_events",
                    )
    async def delete_visitor(
        self,
        user_id: int,
        event_id: int,
    ) -> dict:
        async with self.session() as session:
            obj = await session.execute(
                select(Visitor).filter(
                    Visitor.event_id == event_id and Visitor.user_id == user_id
                )
            )

            try:
                if obj:
                    await session.delete(obj.scalar())
                    await session.commit()
                    return "done"
                raise DataBaseError(
                        detail="delete_visitor",
                    )
            except Exception:
                raise DataBaseError(
                        detail="delete_visitor",
                    )
    async def verify_visitor(self, unique_string: str) -> str:
        async with self.session() as session:
            try:
                obj = await session.execute(
                    select(Visitor).where(Visitor.unique_string == unique_string)
                )
                scalars = obj.scalar()
                return scalars
            except Exception:
                return None
