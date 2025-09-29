"""Berry Flavors endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class BerryFlavor:
    id: int
    name: str
    berries: list[FlavorBerryMap]
    contest_type: NamedAPIResource
    names: list[Name]


@dataclass(frozen=True)
class FlavorBerryMap:
    potency: int
    berry: NamedAPIResource
