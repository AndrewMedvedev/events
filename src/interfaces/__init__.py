__all__ = (
    "CRUDEventBase",
    "CRUDNewsBase",
    "CRUDVisitorBase",
    "EventBase",
    "ImagesBase",
    "NewsBase",
    "VisitorBase",
)

from .crud_interface import CRUDEventBase, CRUDNewsBase, CRUDVisitorBase
from .event_interface import EventBase
from .images_interface import ImagesBase
from .news_interface import NewsBase
from .visitor_interface import VisitorBase
