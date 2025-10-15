from collections.abc import AsyncIterable

from dishka import Provider, Scope, from_context, make_async_container, provide
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from .database.base import create_sessionmaker
from .database.repository import EventRepository, NewsRepository, VisitorRepository
from .services.events import EventService
from .services.news import NewsService
from .services.visitors import VisitorService
from .settings import Settings, settings


class AppProvider(Provider):
    app_settings = from_context(provides=Settings, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_sessionmaker(  # noqa: PLR6301
        self, app_settings: Settings
    ) -> async_sessionmaker[AsyncSession]:
        return create_sessionmaker(app_settings.postgres.url)

    @provide(scope=Scope.REQUEST)
    async def get_session(  # noqa: PLR6301
        self,
        sessionmaker: async_sessionmaker[AsyncSession],
    ) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    def get_visitor_repository(self, session: AsyncSession) -> VisitorRepository:  # noqa: PLR6301
        return VisitorRepository(session=session)

    @provide(scope=Scope.REQUEST)
    def get_event_repository(self, session: AsyncSession) -> EventRepository:  # noqa: PLR6301
        return EventRepository(session=session)

    @provide(scope=Scope.REQUEST)
    def get_news_repository(self, session: AsyncSession) -> NewsRepository:  # noqa: PLR6301
        return NewsRepository(session=session)

    @provide(scope=Scope.REQUEST)
    def get_visitor_service(self, repository: VisitorRepository) -> VisitorService:  # noqa: PLR6301
        return VisitorService(repository)

    @provide(scope=Scope.REQUEST)
    def get_event_service(self, repository: EventRepository) -> EventService:  # noqa: PLR6301
        return EventService(repository)

    @provide(scope=Scope.REQUEST)
    def get_news_service(self, repository: NewsRepository) -> NewsService:  # noqa: PLR6301
        return NewsService(repository)


container = make_async_container(AppProvider(), context={Settings: settings})
