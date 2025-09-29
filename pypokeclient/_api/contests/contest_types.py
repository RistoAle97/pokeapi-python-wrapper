"""Contest Types endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import NamedAPIResource


@dataclass(frozen=True)
class ContestType:
    id: int
    name: str
    berry_flavor: NamedAPIResource
    names: list[ContestName]


@dataclass(frozen=True)
class ContestName:
    name: str
    color: str
    language: NamedAPIResource
