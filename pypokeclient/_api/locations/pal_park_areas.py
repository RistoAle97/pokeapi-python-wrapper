"""Pal Park Areas endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class PalParkArea:
    id: int
    name: str
    names: list[Name]
    pokemon_encounters: list[PalParkEncounterSpecies]


@dataclass(frozen=True)
class PalParkEncounterSpecies:
    base_score: int
    rate: int
    pokemon_species: NamedAPIResource
