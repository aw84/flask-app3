from typing import Optional

from werkzeug.exceptions import HTTPException


class XXXResponse:
    pass


class ApiException(HTTPException):
    def __init__(self, code: Optional[int], description: Optional[str] = None) -> None:
        self.code = code
        super().__init__(description=description, response=None)


class ApiBadRequest(ApiException):
    def __init__(self, description: Optional[str] = None) -> None:
        super().__init__(400, description=description)


class ApiNotFound(ApiException):
    def __init__(self, description: Optional[str] = None) -> None:
        super().__init__(404, description=description)
