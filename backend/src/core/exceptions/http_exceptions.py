# Built-in Dependencies
from http import HTTPStatus

# Third-Party Dependencies
from fastapi import HTTPException, status


class CustomException(HTTPException):
    """
    Custom base exception class for handling HTTP exceptions.

    Parameters
    ----------
    status_code : int, optional
        The HTTP status code for the exception. Defaults to 500 (Internal Server Error).
    detail : str, optional
        A detailed message providing information about the exception. If not provided, it defaults to the description
        associated with the specified status code.
    """

    def __init__(
        self,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail: str | None = None,
    ):
        if not detail:
            detail = HTTPStatus(status_code).description
        super().__init__(status_code=status_code, detail=detail)


class BadRequestException(CustomException):
    """
    Exception for bad client requests (HTTP 400 Bad Request).

    Parameters
    ----------
    detail : str, optional
        A detailed message providing information about the exception.
    """

    def __init__(self, detail: str | None = None):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


class NotFoundException(CustomException):
    """
    Exception for not found resources (HTTP 404 Not Found).

    Parameters
    ----------
    detail : str, optional
        A detailed message providing information about the exception.
    """

    def __init__(self, detail: str | None = None):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class ForbiddenException(CustomException):
    """
    Exception for forbidden access (HTTP 403 Forbidden).

    Parameters
    ----------
    detail : str, optional
        A detailed message providing information about the exception.
    """

    def __init__(self, detail: str | None = None):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)


class UnauthorizedException(CustomException):
    """
    Exception for unauthorized access (HTTP 401 Unauthorized).

    Parameters
    ----------
    detail : str, optional
        A detailed message providing information about the exception.
    """

    def __init__(self, detail: str | None = None):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


class UnprocessableEntityException(CustomException):
    """
    Exception for unprocessable entities (HTTP 422 Unprocessable Entity).

    Parameters
    ----------
    detail : str, optional
        A detailed message providing information about the exception.
    """

    def __init__(self, detail: str | None = None):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)


class DuplicateValueException(CustomException):
    """
    Exception for duplicate values (HTTP 422 Unprocessable Entity).

    Parameters
    ----------
    detail : str, optional
        A detailed message providing information about the exception.
    """

    def __init__(self, detail: str | None = None):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)


class RateLimitException(CustomException):
    """
    Exception for rate limit exceeded (HTTP 429 Too Many Requests).

    Parameters
    ----------
    detail : str, optional
        A detailed message providing information about the exception.
    """

    def __init__(self, detail: str | None = None):
        super().__init__(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=detail)
