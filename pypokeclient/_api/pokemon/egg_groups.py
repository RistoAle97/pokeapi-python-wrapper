"""Egg Groups endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class EggGroup:
    id: int
    name: str
    names: list[Name]
    pokemon_species: list[NamedAPIResource]
