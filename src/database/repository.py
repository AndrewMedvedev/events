from typing import Optional, TypeVar

import os
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import delete, func, insert, select
from sqlalchemy.exc import DataError, IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import UnmappedInstanceError

from ..core.domain import EventSchema, NewsSchema, VisitorSchema
from ..core.exceptions import (
    AlreadyExistsError,
    CreationError,
    DeletionError,
    MismatchError,
    NoPlacesError,
    ReadingError,
)
from ..utils import valid_image
from .base import Base
from .models import EventModel, NewsModel, PointsModel, VisitorModel

ModelT = TypeVar("ModelT", bound=Base)
SchemaT = TypeVar("SchemaT", bound=BaseModel)


class CRUDRepository[ModelT: Base, SchemaT: BaseModel]:
    model: type[ModelT]
    schema: type[SchemaT]

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, schema: SchemaT) -> SchemaT:
        try:
            stmt = insert(self.model).values(**schema.model_dump()).returning(self.model)
            result = await self.session.execute(stmt)
            await self.session.commit()
            created_model = result.scalar_one()
            return self.schema.model_validate(created_model)
        except IntegrityError as e:
            await self.session.rollback()
            raise AlreadyExistsError(f"Already created error: {e}") from e
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise CreationError(f"Error while creation: {e}") from e

    async def read_all(self, limit: int, page: int) -> list[SchemaT]:
        try:
            offset = (page - 1) * limit
            stmt = select(self.model).offset(offset).limit(limit)
            results = await self.session.execute(stmt)
            models = results.scalars().all()
            return [self.schema.model_validate(model) for model in models]
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise ReadingError(f"Error while reading: {e}") from e

    async def delete(self, id: int) -> bool:  # noqa: A002
        try:
            stmt = delete(self.model).where(self.model.id == id)
            result = await self.session.execute(stmt)
            await self.session.commit()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise DeletionError(f"Error while deletion: {e}") from e
        else:
            return result.rowcount > 0


class EventRepository(CRUDRepository[EventModel, EventSchema]):
    model = EventModel
    schema = EventSchema


class NewsRepository(CRUDRepository[NewsModel, NewsSchema]):
    model = NewsModel
    schema = NewsSchema

    async def delete_news(self, news_id: int) -> None:
        stmt = select(NewsModel).filter(NewsModel.id == news_id)
        obj = await self.session.execute(stmt)
        if not obj:
            raise DeletionError
        data = obj.scalar()
        img = valid_image(data.image)
        if img:
            os.remove(data.image)
        await self.session.delete(data)
        await self.session.commit()


class VisitorRepository(CRUDRepository[VisitorModel, VisitorSchema]):
    model = VisitorModel
    schema = VisitorSchema

    async def create_visitors(self, schema: VisitorSchema) -> None:
        try:
            counts = await self.session.scalar(
                select(EventModel.limit_people).where(EventModel.id == schema.event_id)
            )
            counts_visitors = await self.session.execute(
                select(func.count())
                .select_from(VisitorModel)
                .filter(VisitorModel.event_id == schema.event_id)
            )

            if counts_visitors.scalar() < counts or counts == 0:
                stmt = insert(self.model).values(**schema.model_dump()).returning(self.model)
                await self.session.execute(stmt)
                await self.session.commit()
            else:
                raise NoPlacesError
        except DataError:
            raise MismatchError from None
        except IntegrityError:
            raise CreationError from None

    async def get_visitors_events(self, user_id: UUID) -> list[VisitorSchema]:
        result = (
            (
                await self.session.execute(
                    select(VisitorModel).filter(VisitorModel.user_id == user_id)
                )
            )
            .scalars()
            .all()
        )
        return [self.schema.model_validate(visitor) for visitor in result]

    async def delete_visitors(self, user_id: UUID, event_id: int) -> None:
        try:
            obj = await self.session.execute(
                select(VisitorModel).filter(
                    VisitorModel.event_id == event_id and VisitorModel.user_id == user_id
                )
            )

            if not obj:
                raise DeletionError

            await self.session.delete(obj.scalar())
            await self.session.commit()
        except UnmappedInstanceError:
            raise DeletionError from None

    async def verify_visitors(self, unique_string: str) -> Optional[VisitorModel]:
        obj = await self.session.execute(
            select(VisitorModel)
            .options(joinedload(VisitorModel.event))
            .where(VisitorModel.unique_string == unique_string)
        )
        data_visitor = obj.scalar()
        if data_visitor:
            event_points = data_visitor.event.points_for_the_event
            await self.visitor_check_in_points_table(
                session=self.session, user_id=data_visitor.user_id, event_points=event_points
            )
        else:
            return None
        await self.session.commit()
        return data_visitor

    @staticmethod
    async def visitor_check_in_points_table(
        session: AsyncSession, user_id: UUID, event_points: float
    ) -> None:
        points_visitor = (
            await session.execute(select(PointsModel).where(PointsModel.user_id == user_id))
        ).scalar()
        if points_visitor is None:
            session.add(PointsModel(user_id=user_id, points=event_points))
        else:
            points_visitor.points += event_points
