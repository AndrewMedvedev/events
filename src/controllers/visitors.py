from ..database.crud import SQLVisitor
from ..exeptions import BadRequestHTTPError
from ..rest import get_user_data
from ..schemas import UserEventSchema, VisitorSchema


class VisitorsControl:
    def __init__(self):
        self.sql_visitor = SQLVisitor()

    async def create_user(self, user_id: int, event_id: int) -> None:
        if (data := await get_user_data(user_id)).get("body") is None:
            raise BadRequestHTTPError()

        result = VisitorSchema.create({"user_id": user_id, "event_id": event_id, **data["body"]})
        return await self.sql_visitor.create_visitors(result.to_model())

    async def get_user_events(self, user_id: int) -> UserEventSchema:
        return UserEventSchema.create(await self.sql_visitor.get_visitors_events(user_id))

    async def delete_user(self, user_id: int, event_id: int) -> None:
        return await self.sql_visitor.delete_visitors(user_id=user_id, event_id=event_id)

    async def verify(self, request, unique_string: str) -> dict | None:
        verify_unique_string = await self.sql_visitor.verify_visitors(
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
