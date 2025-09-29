"""Growth Rates endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Description, NamedAPIResource


@dataclass(frozen=True)
class GrowthRate:
    id: int
    name: str
    formula: str
    descriptions: list[Description]
    levels: list[GrowthRateExperienceLevel]
    pokemon_species: list[NamedAPIResource]


@dataclass(frozen=True)
class GrowthRateExperienceLevel:
    level: int
    experience: int
