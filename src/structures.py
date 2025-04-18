from __future__ import annotations

from dataclasses import dataclass


@dataclass
class JSONError:
    message: str
    description: str
    error: Exception

    @classmethod
    def create(cls, exception: Exception, description: str = None) -> JSONError:
        return cls(message=getattr(exception, "message", str(exception)), description=description if isinstance(description, str) else "", error=exception)

    def to_dict(self):
        return {"message": self.message, "description": self.description, "error": f"{type(self.error)} - {self.error}"}
