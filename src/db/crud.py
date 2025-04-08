import os

from sqlalchemy import func, select

from ..exceptions import DataBaseError
from ..schemas import EventListResponse, NewsListResponse
from ..utils import valid_image
from .models import EventModel, NewsModel, VisitorModel
from .session import db_session


async def create_event(model: EventModel) -> None:
    async with db_session.session() as session:
        session.add(model)
        await session.commit()
        await session.refresh(model)


async def read_event() -> EventListResponse:
    async with db_session.session() as session:
        events = await session.execute(select(EventModel))
    return EventListResponse(events=events.scalars().all())


async def read_events_with_limit(page: int = 1, limit: int = 5) -> EventListResponse:
    offset = (page - 1) * limit
    async with db_session.session() as session:
        stmt = select(EventModel).offset(offset).limit(limit)
        events = await session.execute(stmt)
    return EventListResponse(events=events.scalars().all())


async def delete_event(model_id: int) -> None:
    async with db_session.session() as session:
        obj = await session.get(EventModel, model_id)
        if not obj:
            raise DataBaseError()
        await session.delete(obj)
        await session.commit()


async def create_news(model: NewsModel) -> None:
    async with db_session.session() as session:
        session.add(model)
        await session.commit()
        await session.refresh(model)


async def read_news() -> NewsListResponse:
    async with db_session.session() as session:
        news = await session.execute(select(NewsModel))
    return NewsListResponse(news=news.scalars().all())


async def read_news_with_limit(page: int = 1, limit: int = 5) -> NewsListResponse:
    offset = (page - 1) * limit
    async with db_session.session() as session:
        stmt = select(NewsModel).offset(offset).limit(limit)
        news = await session.execute(stmt)
    return NewsListResponse(news=news.scalars().all())


async def delete_news(news_id: int) -> None:
    async with db_session.session() as session:
        obj = await session.execute(select(NewsModel).filter(NewsModel.id == news_id))
        if not obj:
            raise DataBaseError()
        data = obj.scalar()
        img = await valid_image(data.image)
        if img:
            os.remove(data.image)
        await session.delete(data)
        await session.commit()


async def create_visitor(model: VisitorModel) -> None:
    async with db_session.session() as session:
        counts = await session.scalar(select(EventModel.limit_people).where(EventModel.id == model.event_id))
        counts_visitors = await session.execute(
            select(func.count()).select_from(VisitorModel).filter(VisitorModel.event_id == model.event_id))

        if counts_visitors.scalar() > counts or counts != 0:
            raise DataBaseError()

        session.add(model)
        await session.commit()
        await session.refresh(model)


async def get_visitors_events(user_id: int) -> list:
    async with db_session.session() as session:
        return await session.execute(select(VisitorModel).filter(VisitorModel.user_id == user_id)).scalars().all()


async def delete_visitor(user_id: int, event_id: int) -> None:
    async with db_session.session() as session:
        obj = await session.execute(
            select(VisitorModel).filter(VisitorModel.event_id == event_id and VisitorModel.user_id == user_id))

        if not obj:
            raise DataBaseError()

        await session.delete(obj.scalar())
        await session.commit()


async def verify_visitor(unique_string: str) -> VisitorModel:
    async with db_session.session() as session:
        obj = await session.execute(select(VisitorModel).where(VisitorModel.unique_string == unique_string))
        scalars = obj.scalar()
    return scalars
