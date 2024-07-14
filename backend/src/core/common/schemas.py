# Built-in Dependencies
from typing import Generic, TypeVar, List

# Third-Party Dependencies
from pydantic import BaseModel

# Generic type variable for the schema used in the list response
SchemaType = TypeVar("SchemaType", bound=BaseModel)


# Generic BaseModel for a list response
class ListResponse(BaseModel, Generic[SchemaType]):
    """
    Description:
    ----------
    Schema for representing a list response.

    Fields:
    ----------
    - 'data' (List[SchemaType]): List of items in the response.
    """

    data: List[SchemaType]


# BaseModel for a paginated list response, inheriting from the generic ListResponse
class PaginatedListResponse(ListResponse[SchemaType]):
    """
    Description:
    ----------
    Schema for representing a paginated list response.

    Fields:
    ----------
    - 'data' (List[SchemaType]): List of items in the response.
    - 'total_count' (int): Total number of items.
    - 'has_more' (bool): Whether there are more items beyond the current page.
    - 'page' (int | None): Current page number.
    - 'items_per_page' (int | None): Number of items per page.
    """

    total_count: int  # Total number of items
    has_more: bool  # Whether there are more items beyond the current page
    page: int | None = None  # Current page number
    items_per_page: int | None = None  # Number of items per page
