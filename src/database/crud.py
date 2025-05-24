from typing import Optional

import os
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.exc import DataError, IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import UnmappedInstanceError

from ..exeptions import BadRequestHTTPError, ExistsHTTPError, NoPlacesHTTPError
from ..schemas import EventListResponse, NewsListResponse
from ..utils import valid_image
from .models import EventModel, NewsModel, PointsModel, VisitorModel
from .session import DatabaseSessionService


class SQLEvent(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_events(self, model: EventModel) -> None:
        try:
            async with self.session() as session:
                session.add(model)
                await session.commit()
                await session.refresh(model)
        except DataError:
            raise BadRequestHTTPError from None
        except IntegrityError:
            raise ExistsHTTPError from None

    async def read_events(
        self,
    ) -> EventListResponse:
        async with self.session() as session:
            events = await session.execute(select(EventModel))
        return EventListResponse(events=events.scalars().all())

    async def read_events_with_limit(self, page: int = 1, limit: int = 5) -> EventListResponse:
        offset = (page - 1) * limit
        async with self.session() as session:
            stmt = select(EventModel).offset(offset).limit(limit)
            events = await session.execute(stmt)
        return EventListResponse(events=events.scalars().all())

    async def delete_events(self, model_id: int) -> None:
        async with self.session() as session:
            obj = await session.get(EventModel, model_id)
            if not obj:
                raise BadRequestHTTPError
            await session.delete(obj)
            await session.commit()


class SQLNews(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_news(self, model: NewsModel) -> None:
        try:
            async with self.session() as session:
                session.add(model)
                await session.commit()
                await session.refresh(model)
        except DataError:
            raise BadRequestHTTPError from None
        except IntegrityError:
            raise ExistsHTTPError from None

    async def read_news(
        self,
    ) -> NewsListResponse:
        async with self.session() as session:
            news = await session.execute(select(NewsModel))
        return NewsListResponse(news=news.scalars().all())

    async def read_news_with_limit(self, page: int = 1, limit: int = 5) -> NewsListResponse:
        offset = (page - 1) * limit
        async with self.session() as session:
            stmt = select(NewsModel).offset(offset).limit(limit)
            news = await session.execute(stmt)
        return NewsListResponse(news=news.scalars().all())

    async def delete_news(self, news_id: int) -> None:
        async with self.session() as session:
            obj = await session.execute(select(NewsModel).filter(NewsModel.id == news_id))
            if not obj:
                raise BadRequestHTTPError
            data = obj.scalar()
            img = valid_image(data.image)
            if img:
                os.remove(data.image)
            await session.delete(data)
            await session.commit()


class SQLVisitor(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_visitors(self, model: VisitorModel) -> None:
        try:
            async with self.session() as session:
                counts = await session.scalar(
                    select(EventModel.limit_people).where(EventModel.id == model.event_id)
                )
                counts_visitors = await session.execute(
                    select(func.count())
                    .select_from(VisitorModel)
                    .filter(VisitorModel.event_id == model.event_id)
                )

                if counts_visitors.scalar() < counts or counts == 0:
                    session.add(model)
                    await session.commit()
                    await session.refresh(model)
                else:
                    raise NoPlacesHTTPError
        except DataError:
            raise BadRequestHTTPError from None
        except IntegrityError:
            raise ExistsHTTPError from None

    async def get_visitors_events(self, user_id: UUID) -> list:
        async with self.session() as session:
            return (
                (
                    await session.execute(
                        select(VisitorModel).filter(VisitorModel.user_id == user_id)
                    )
                )
                .scalars()
                .all()
            )

    async def delete_visitors(self, user_id: UUID, event_id: int) -> None:
        try:
            async with self.session() as session:
                obj = await session.execute(
                    select(VisitorModel).filter(
                        VisitorModel.event_id == event_id and VisitorModel.user_id == user_id
                    )
                )

                if not obj:
                    raise BadRequestHTTPError

                await session.delete(obj.scalar())
                await session.commit()
        except UnmappedInstanceError:
            raise BadRequestHTTPError from None

    async def verify_visitors(self, unique_string: str) -> Optional[VisitorModel]:
        async with self.session() as session:
            obj = await session.execute(
                select(VisitorModel)
                .options(joinedload(VisitorModel.event))
                .where(VisitorModel.unique_string == unique_string)
            )
            data_visitor = obj.scalar()
            if data_visitor:
                event_points = data_visitor.event.points_for_the_event
                await self.visitor_check_in_points_table(
                    session=session, user_id=data_visitor.user_id, event_points=event_points
                )
            else:
                return None
            await session.commit()
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
