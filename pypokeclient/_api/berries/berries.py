"""Berries endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import NamedAPIResource


@dataclass(frozen=True)
class Berry:
    id: int
    name: str
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    size: int
    smoothness: int
    soil_dryness: int
    firmness: NamedAPIResource
    flavors: list[BerryFlavorMap]
    item: NamedAPIResource
    natural_gift_type: NamedAPIResource


@dataclass(frozen=True)
class BerryFlavorMap:
    potency: int
    flavor: NamedAPIResource
