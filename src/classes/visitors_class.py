from fastapi import Response, status
from fastapi.responses import JSONResponse

from src.classes.valid_tokens import ValidTokens
from src.database import get_data
from src.database.models import Visitor
from src.database.services.crud import CRUD


class Visitors:

    def __init__(
        self,
        token_access: str,
        token_refresh: str,
        response: Response,
        event_id: int = None,
    ) -> None:
        self.token_access = token_access
        self.token_refresh = token_refresh
        self.event_id = event_id
        self.response = response

    async def add_user(self) -> JSONResponse:
        check_tokens = await ValidTokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        data = await get_data(check_tokens.get("user_id"))
        user_model = Visitor(
            user_id=check_tokens.get("user_id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            event_id=self.event_id,
        )
        await CRUD().create_visitor(user_model)
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite=None,
                httponly=False,
                secure=True,
            )
        return JSONResponse(content=status.HTTP_200_OK)

    async def get_user_events(self) -> list[dict]:
        check_tokens = await ValidTokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        events = await CRUD().get_visitors_events(user_id=check_tokens.get("user_id"))
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite=None,
                httponly=False,
                secure=True,
            )
        return [{"event_id": i.event_id} for i in events]

    async def delete_user(self) -> JSONResponse:
        check_tokens = await ValidTokens(
            token_access=self.token_access,
            token_refresh=self.token_refresh,
            response=self.response,
        ).valid()
        await CRUD().delete_visitor(
            user_id=check_tokens.get("user_id"), event_id=self.event_id
        )
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite=None,
                httponly=False,
                secure=True,
            )
        return JSONResponse(content=status.HTTP_200_OK)
