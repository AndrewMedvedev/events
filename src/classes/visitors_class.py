import logging
import uuid

from fastapi.responses import HTMLResponse, JSONResponse

from src.database import get_user_data
from src.database.models import Visitor
from src.database.services.crud import CRUD
from src.interfaces import VisitorBase

log = logging.getLogger(__name__)


class Visitors(VisitorBase):

    def __init__(self) -> None:
        self.crud = CRUD()
        self.visitor = Visitor

    async def add_user(
        self,
        user_id: int,
        event_id: int,
    ) -> JSONResponse:
        data = await get_user_data(
            user_id,
        )
        user_model_visitor = self.visitor(
            user_id=user_id,
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            event_id=event_id,
            unique_string=f"{str(uuid.uuid4())}{str(uuid.uuid4())}",
        )
        return JSONResponse(content=await self.crud.create_visitor(user_model_visitor))

    async def get_user_events(
        self,
        user_id: int,
    ) -> list[dict]:
        events = await self.crud.get_visitors_events(
            user_id=user_id,
        )
        return [
            {
                "event_id": i.event_id,
                "unique_string": i.unique_string,
            }
            for i in events
        ]

    async def delete_user(
        self,
        user_id: int,
        event_id: int,
    ) -> JSONResponse:
        delete = await self.crud.delete_visitor(
            user_id=user_id,
            event_id=event_id,
        )
        return JSONResponse(
            content=delete,
        )

    async def verify(
        self,
        unique_string: str,
    ) -> HTMLResponse:
        verify_unique_string = await self.crud.verify_visitor(
            unique_string=unique_string,
        )
        if verify_unique_string is not None:
            html_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Зарегистрирован</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #000000 0%, #24a304 100%);
            font-family: 'Arial', sans-serif;
        }}
        
        .registration-banner {{
            width: 100%;
            max-width: 400px;
            text-align: center;
            color: #ffffff;
        }}
        
        .banner-title {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 25px;
        }}
        
        .user-info {{
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(21, 252, 0, 0.05);
        }}
        
        .info-row {{
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            margin: 10px 0;
            border-bottom: 1px solid #eee;
        }}
        
        .info-row:last-child {{
            border-bottom: none;
        }}
        
        .info-label {{
            font-weight: bold;
            color: #000000;
        }}
        
        .info-value {{
            color: #000000;
        }}
    </style>
</head>
<body>
    <div class="registration-banner">
        <div class="banner-title">Зарегистрирован</div>
        
        <div class="user-info">
            <div class="info-row">
                <span class="info-label">Имя:</span>
                <span class="info-value">{verify_unique_string.first_name}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Фамилия:</span>
                <span class="info-value">{verify_unique_string.last_name}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Email:</span>
                <span class="info-value">{verify_unique_string.email}</span>
            </div>
        </div>
    </div>
</body>
</html>"""
            return HTMLResponse(content=html_content)
        else:
            html_content = """<!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Не Зарегистрирован</title>
                <style> body { font-family: Arial, Helvetica, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; background-color: #000000; margin: 0; } .message-container { background-color: #b30606; padding: 40px; border-radius: 10px; box-shadow: 0 10px 20px rgb(0, 0, 0); text-align: center; } h1 { font-size: 32px; color: #ffffff; margin-bottom: 20px; } p { font-size: 18px; color: #000000; } </style>
            </head>
            <body>
                <div class="message-container">
                    <h1>Не Зарегистрирован</h1>
                </div>
            </body>
            </html>"""
            return HTMLResponse(content=html_content)
