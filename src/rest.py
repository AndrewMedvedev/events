from uuid import UUID

import aiohttp

from config import settings

from .utils import valid_answer


async def get_user_data(user_id: UUID) -> dict:
    async with (
        aiohttp.ClientSession() as session,
        session.get(url=f"{settings.GET_DATA}{user_id}", ssl=False) as data,
    ):
        return await valid_answer(response=data)
