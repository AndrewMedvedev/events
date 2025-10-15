from uuid import UUID

from ..core.domain import VisitorSchema
from ..database.repository import VisitorRepository
from ..exeptions import BadRequestHTTPError
from ..rest import get_user_data


class VisitorService:
    def __init__(self, repository: VisitorRepository):
        self.repository = repository

    async def create_user(self, user_id: UUID, event_id: int) -> None:
        if (data := await get_user_data(user_id)) is None:
            raise BadRequestHTTPError
        result = VisitorSchema(**data, user_id=user_id, event_id=event_id)
        return await self.repository.create_visitors(result)

    async def get_user_events(self, user_id: UUID) -> list[VisitorSchema]:
        return await self.repository.get_visitors_events(user_id)

    async def delete_user(self, user_id: UUID, event_id: int) -> None:
        return await self.repository.delete_visitors(user_id, event_id)

    async def verify(self, request, unique_string: str) -> dict | None:
        verify_unique_string = await self.repository.verify_visitors(
            unique_string=unique_string,
        )
        if verify_unique_string is None:
            return None

        return {
            "request": request,
            "first_name": verify_unique_string.first_name,
            "last_name": verify_unique_string.last_name,
            "email": verify_unique_string.email,
        }
