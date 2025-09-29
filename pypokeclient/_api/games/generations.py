"""Generations endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class Generation:
    id: int
    name: str
    abilities: list[NamedAPIResource]
    names: list[Name]
    main_region: NamedAPIResource
    moves: list[NamedAPIResource]
    pokemon_species: list[NamedAPIResource]
    types: list[NamedAPIResource]
    version_groups: list[NamedAPIResource]
