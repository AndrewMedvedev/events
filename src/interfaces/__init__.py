__all__ = (
    "CRUDEventBase",
    "CRUDVisitorBase",
    "CRUDNewsBase",
    "EventBase",
    "VisitorBase",
    "NewsBase",
)

from src.interfaces.crud_interface import (CRUDEventBase, CRUDNewsBase,
                                           CRUDVisitorBase)
from src.interfaces.event_interface import EventBase
from src.interfaces.visitor_interface import VisitorBase

from .news_interface import NewsBase
