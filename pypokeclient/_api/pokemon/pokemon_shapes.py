"""Pokemon Shapes endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class PokemonShape:
    id: int
    name: str
    awesome_names: list[AwesomeName]
    names: list[Name]
    pokemon_species: list[NamedAPIResource]


@dataclass(frozen=True)
class AwesomeName:
    awesome_name: str
    language: NamedAPIResource
