"""Version Groups endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import NamedAPIResource


@dataclass(frozen=True)
class VersionGroup:
    id: int
    name: str
    order: int
    generation: NamedAPIResource
    move_learn_methods: list[NamedAPIResource]
    pokedexes: list[NamedAPIResource]
    regions: list[NamedAPIResource]
    versions: list[NamedAPIResource]
