import aiohttp

from src.config import Settings


async def get_data(params: dict) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            Settings.GET_DATA,
            params=params,
            ssl=False,
        ) as data:
            user_data = await data.json()
            return user_data
