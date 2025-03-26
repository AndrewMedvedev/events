class DataBaseError(Exception):

    def __init__(
        self,
        name: str,
        message: str,
    ) -> None:
        self.name = name
        self.message = message
        super().__init__(self.name)

    def __str__(self) -> str:
        return f"{self.name}, {self.message}"


class SendError(Exception):

    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(self.name)

    def __str__(self) -> str:
        return f"Ошибка в методе {self.name}. Пришли неверные данные"
