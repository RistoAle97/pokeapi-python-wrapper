"""Locations endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import GenerationGameIndex, Name, NamedAPIResource


@dataclass(frozen=True)
class Location:
    id: int
    name: str
    region: NamedAPIResource | None
    names: list[Name]
    game_indices: list[GenerationGameIndex]
    areas: list[NamedAPIResource]
