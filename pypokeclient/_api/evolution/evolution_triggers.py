"""Evolution Trigger endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class EvolutionTrigger:
    id: int
    name: str
    names: list[Name]
    pokemon_species: list[NamedAPIResource]
