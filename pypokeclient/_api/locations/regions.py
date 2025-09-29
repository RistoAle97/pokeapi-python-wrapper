"""Regions endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class Region:
    id: int
    locations: list[NamedAPIResource]
    name: str
    names: list[Name]
    main_generation: NamedAPIResource | None
    pokedexes: list[NamedAPIResource]
    version_groups: list[NamedAPIResource]
