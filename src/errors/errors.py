class DataBaseError(Exception):

    def __init__(self, detail: str) -> None:
        self.detail = detail
        super().__init__(self.detail)

    def __str__(self) -> str:
        return self.detail


class SendError(Exception):

    def __init__(self, detail: str) -> None:
        self.detail = detail
        super().__init__(self.detail)

    def __str__(self) -> str:
        return self.detail


class ImageAddError(Exception):

    def __init__(self, detail: str) -> None:
        self.detail = detail
        super().__init__(self.detail)

    def __str__(self) -> str:
        return self.detail
    

class ImageGetError(Exception):

    def __init__(self, detail: str) -> None:
        self.detail = detail
        super().__init__(self.detail)

    def __str__(self) -> str:
        return self.detail
