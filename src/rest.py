import aiohttp

from config import Settings

from .utils import valid_answer


async def get_user_data(user_id: int) -> dict:
    async with aiohttp.ClientSession() as session, session.get(
        url=f"{Settings.GET_DATA}{user_id}", ssl=False
    ) as data:
        return await valid_answer(response=data)
