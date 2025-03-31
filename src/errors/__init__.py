__all__ = (
    "DataBaseError",
    "SendError",
    "db_error",
    "send_error",
)

from .errors import DataBaseError, SendError
from .func_errors import db_error, send_error
