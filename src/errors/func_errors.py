from fastapi import Request, status

from src.responses import CustomBadResponse

from .errors import DataBaseError, SendError


async def db_error(
    request: Request,
    exc: DataBaseError,
) -> CustomBadResponse:
    return CustomBadResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message=str(exc),
        detail="Ошибка базы данных",
    )


async def send_error(
    request: Request,
    exc: SendError,
) -> CustomBadResponse:
    return CustomBadResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        message=str(exc),
        detail="Были введены неверные данные",
    )
