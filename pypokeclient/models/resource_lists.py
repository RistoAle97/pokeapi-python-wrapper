"""Resource Lists/Pagination endpoint."""

from pydantic.dataclasses import dataclass

from .common_models import APIResource, NamedAPIResource


@dataclass(frozen=True)
class NamedAPIResourceList:
    """Represent a paginated list of named API resources returned by PokéAPI.

    This model represents collection responses containing named resources, with pagination metadata for retrieving
    additional results.

    Attributes:
        count (int): The total number of resources available in the collection.
        next (str | None): The URL of the next page of results, or `None` if there are no further results.
        previous (str | None): The URL of the previous page of results, or `None` if there is no previous page.
        results (list[NamedAPIResource]): The named resources returned on the current page.
    """

    count: int
    next: str | None
    previous: str | None
    results: list[NamedAPIResource]


@dataclass(frozen=True)
class APIResourceList:
    """Represent a paginated list of API resources returned by PokéAPI.

    This model represents collection responses containing resources without names, with pagination metadata for
    retrieving additional results.

    Attributes:
        count (int): The total number of resources available in the collection.
        next (str | None): The URL of the next page of results, or `None` if there are no further results.
        previous (str | None): The URL of the previous page of results, or `None` if there is no previous page.
        results (list[APIResource]): The resources returned on the current page.
    """

    count: int
    next: str | None
    previous: str | None
    results: list[APIResource]
