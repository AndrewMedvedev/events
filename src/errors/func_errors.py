from fastapi import Request, status

from src.responses import CustomBadResponse

from .errors import DataBaseError, ImageAddError, ImageGetError, SendError


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


async def image_add_error(
    request: Request,
    exc: ImageAddError,
) -> CustomBadResponse:
    return CustomBadResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        message=str(exc),
        detail="Неверный формат",
    )


async def image_get_error(
    request: Request,
    exc: ImageGetError,
) -> CustomBadResponse:
    return CustomBadResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message=str(exc),
        detail="Невозможно получить изображение",
    )
