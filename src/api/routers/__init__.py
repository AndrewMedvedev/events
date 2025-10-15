__all__ = (
    "events",
    "news",
    "visitors",
)

from fastapi import APIRouter

from .events import events
from .news import news
from .visitors import visitors

router = APIRouter(prefix="/api/v1")
router.include_router(visitors)
router.include_router(events)
router.include_router(news)
