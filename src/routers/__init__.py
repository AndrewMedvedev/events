__all__ = (
    "router_event",
    "router_visitors",
    "router_news",
)

from .events_routers import router_event
from .news_router import router_news
from .visitors_routers import router_visitors
