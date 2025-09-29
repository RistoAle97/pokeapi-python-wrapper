"""Pokedexes endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Description, Name, NamedAPIResource


@dataclass(frozen=True)
class Pokedex:
    id: int
    name: str
    is_main_series: bool
    descriptions: list[Description]
    names: list[Name]
    pokemon_entries: list[PokemonEntry]
    region: NamedAPIResource | None
    version_groups: list[NamedAPIResource]


@dataclass(frozen=True)
class PokemonEntry:
    entry_number: int
    pokemon_species: NamedAPIResource
