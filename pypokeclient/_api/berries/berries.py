"""Berries endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import NamedAPIResource


@dataclass(frozen=True)
class Berry:
    id: int
    name: str
    growth_time: int | None
    max_harvest: int | None
    natural_gift_power: int | None
    size: int | None
    smoothness: int | None
    soil_dryness: int | None
    firmness: NamedAPIResource
    flavors: list[BerryFlavorMap]
    item: NamedAPIResource
    natural_gift_type: NamedAPIResource


@dataclass(frozen=True)
class BerryFlavorMap:
    potency: int
    flavor: NamedAPIResource
