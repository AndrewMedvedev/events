import json

import aiohttp
from fastapi import Response

from src.config import Settings


class ValidTokens:

    def __init__(
        self,
        token_access: str,
        token_refresh: str,
        response: Response,
    ) -> None:
        self.token_access = token_access
        self.token_refresh = token_refresh
        self.response = response

    async def valid(self) -> dict | str:
        send_access = await self.send_access_token(self.token_access)
        send_refresh = await self.send_refresh_token(self.token_refresh)
        try:
            match send_access:
                case dict():
                    return send_access
                case _:
                    if isinstance(send_refresh, dict):
                        self.response.delete_cookie(
                            key="access",
                            samesite=None,
                            httponly=False,
                            secure=True,
                        )
                        return send_refresh
        except Exception as e:
            return e

    @staticmethod
    async def send_refresh_token(
        token_refresh: str,
    ) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=f"{Settings.VALIDATE_REFRESH}{token_refresh}",
            ) as response:
                token = await response.text()
                return json.loads(token)

    @staticmethod
    async def send_access_token(
        token_access: str,
    ) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=f"{Settings.VALIDATE_ACCESS}{token_access}",
            ) as response:
                token = await response.text()
                return token
