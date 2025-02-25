import aiohttp

from src.config import Settings


async def get_data(id: int) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url=f"{Settings.GET_DATA}{id}",
            ssl=False,
        ) as data:
            user_data = await data.json()
            return user_data
