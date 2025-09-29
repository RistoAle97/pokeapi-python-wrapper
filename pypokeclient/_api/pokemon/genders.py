"""Genders endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import NamedAPIResource


@dataclass(frozen=True)
class Gender:
    id: int
    name: str
    pokemon_species_details: list[PokemonSpeciesGender]
    required_for_evolution: list[NamedAPIResource]


@dataclass(frozen=True)
class PokemonSpeciesGender:
    rate: int
    pokemon_species: NamedAPIResource
