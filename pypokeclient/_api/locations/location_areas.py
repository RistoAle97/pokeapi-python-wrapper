"""Location Areas endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource, VersionEncounterDetail


@dataclass(frozen=True)
class LocationArea:
    id: int
    name: str
    game_index: int
    encounter_method_rates: list[EncounterMethodRate]
    location: NamedAPIResource
    names: list[Name]
    pokemon_encounters: list[PokemonEncounter]


@dataclass(frozen=True)
class EncounterMethodRate:
    encounter_method: NamedAPIResource
    version_details: list[EncounterVersionDetails]


@dataclass(frozen=True)
class EncounterVersionDetails:
    rate: int
    version: NamedAPIResource


@dataclass(frozen=True)
class PokemonEncounter:
    pokemon: NamedAPIResource
    version_details: list[VersionEncounterDetail]
