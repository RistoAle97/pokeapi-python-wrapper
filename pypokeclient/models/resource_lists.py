"""Resource Lists/Pagination endpoint."""

from pydantic.dataclasses import dataclass

from .common_models import APIResource, NamedAPIResource


@dataclass(frozen=True)
class NamedAPIResourceList:
    count: int
    next: str | None
    previous: str | None
    results: list[NamedAPIResource]


@dataclass(frozen=True)
class APIResourceList:
    count: int
    next: str | None
    previous: str | None
    results: list[APIResource]
