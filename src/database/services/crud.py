from pydantic import BaseModel
from sqlalchemy import select

from src.database.models import Event, PointsEvent, Visitor
from src.database.services.orm import DatabaseSessionService


class CRUD(DatabaseSessionService):
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
                return {"message": 200}
            except Exception as e:
                print(e)

    async def read_event(self) -> list[dict]:
        async with self.session() as session:
            events = await session.execute(select(Event))
        try:
            return events.scalars().all()
        except Exception as _ex:
            print(_ex)
            return _ex

    async def update_event(self, event_id: int, values: BaseModel) -> dict:
        try:
            event = Event(
                id=event_id,
                date_time=values.date_time,
                location=values.location,
                description=values.description,
                limit_people=values.limit_people,
            )
            async with self.session() as session:
                await session.merge(event)
                await session.commit()
                return {"message": 200}
        except Exception as _ex:
            print(_ex)
            return _ex

    async def delete_event(
        self,
        model_id: int,
    ) -> dict | str:
        async with self.session() as session:
            obj = await session.get(Event, model_id)
            try:
                if obj:
                    await session.delete(obj)
                    await session.commit()
                    return {"message": 200}
            except Exception as e:
                print(e)
                return e

    async def create_visitor(
        self,
        model: Visitor,
    ) -> dict:
        async with self.session() as session:
            session.add(model)
            await session.commit()
            await session.refresh(model)
        return {"message": 200}

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
            except Exception as _ex:
                print(_ex)
                return _ex

    async def delete_visitor(
        self,
        user_id: int,
        event_id: int,
    ) -> dict | str:
        async with self.session() as session:
            obj = await session.execute(
                select(Visitor).where(
                    Visitor.user_id == user_id and Visitor.event_id == event_id
                )
            )
            try:
                if obj:
                    await session.delete(obj.scalar())
                    await session.commit()
                    return {"message": 200}
            except Exception as e:
                print(e)
                return e

    async def verify_visitor(self, unique_string: str) -> str:
        async with self.session() as session:
            obj = await session.execute(
                select(Visitor).where(Visitor.unique_string == unique_string)
            )
            return obj.scalar()

    async def get_visitor_unique_string(self, user_id: int, event_id: int) -> str:
        async with self.session() as session:
            obj = await session.execute(
                select(Visitor).where(
                    Visitor.event_id == event_id and Visitor.user_id == user_id
                )
            )
            try:
                unique = obj.scalar()
                return unique.unique_string
            except Exception as e:
                print(e)
                return e

    # async def create_points(self, model: PointsEvent) -> dict:
    #     async with self.session() as session:
    #         try:
    #             session.add(model)
    #             await session.commit()
    #             await session.refresh(model)
    #             return {"message": 200}
    #         except Exception as e:
    #             print(e)

    # async def add_points(self, user_id: int, point: int) -> dict:
    #     async with self.session() as session:
    #         obj = (
    #             await session.execute(
    #                 select(PointsEvent).where(PointsEvent.user_id == user_id)
    #             )
    #         ).scalar()
    #         try:
    #             if obj:
    #                 obj.points += point
    #                 await session.commit()
    #                 return {"message": 200}
    #         except Exception as e:
    #             print(e)
