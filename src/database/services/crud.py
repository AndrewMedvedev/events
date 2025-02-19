from fastapi.responses import JSONResponse
from fastapi import status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from src.database.models import Event
from src.database.schemas import EventModel
from src.database.services.orm import DatabaseSessionService


class CRUD(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_event(
        self,
        model: Event,
    ) -> JSONResponse:
        async with self.session() as session:
            session.add(model)
            await session.commit()
            await session.refresh(model)
        return JSONResponse(status_code=status.HTTP_200_OK)

    async def read_event(self) -> dict:
        async with self.session() as session:
            events = await session.execute(select(Event))
        try:
            return events.scalars().all()
        except Exception as _ex:
            print(_ex)

    async def update_event(
        self,
        model_id: int,
        model: Event,
        values: BaseModel,
    ) -> JSONResponse:
        async with self.session() as session:
            values_dict = values.model_dump(exclude_unset=True)
            try:
                record = await session.get(model, model_id)
                for key, value in values_dict.items():
                    setattr(record, key, value)
                await session.flush()
                return JSONResponse(status_code=status.HTTP_200_OK)
            except SQLAlchemyError as e:
                print(e)
                return JSONResponse(content=e)

    async def delete_event(
        self,
        model_id: int,
        model: Event,
    ) -> JSONResponse:
        async with self.session() as session:
            obj = await session.get(model, model_id)
            try:
                if obj:
                    await session.delete(obj)
                    await session.commit()
                    return JSONResponse(status_code=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return JSONResponse(content=e)
