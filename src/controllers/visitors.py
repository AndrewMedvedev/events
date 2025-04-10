from ..database.crud import CRUD
from ..exeptions import UserDataNotFoundError
from ..rest import get_user_data
from ..schemas import UserEventSchema, VisitorSchema


class VisitorsControl:
    @staticmethod
    async def create_user(user_id: int, event_id: int) -> None:
        if (data := await get_user_data(user_id)).get("body") is None:
            raise UserDataNotFoundError("User data not found or invalid")

        result = VisitorSchema.create({"user_id": user_id, "event_id": event_id, **data["body"]})
        return await CRUD().create_visitor(result.to_model())

    @staticmethod
    async def get_user_events(user_id: int) -> UserEventSchema:
        return UserEventSchema.create(await CRUD().get_visitors_events(user_id))

    @staticmethod
    async def delete_user(user_id: int, event_id: int) -> None:
        return await CRUD().delete_visitor(user_id=user_id, event_id=event_id)

    @staticmethod
    async def verify(request, unique_string: str) -> dict | None:
        verify_unique_string = await CRUD().verify_visitor(
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
