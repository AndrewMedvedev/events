from uuid import UUID


async def get_user_data(user_id: UUID) -> dict:
    return {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
    }


""""
user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
"""
