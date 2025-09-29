"""Move Damage Classes endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Description, Name, NamedAPIResource


@dataclass(frozen=True)
class MoveDamageClass:
    id: int
    name: str
    descriptions: list[Description]
    moves: list[NamedAPIResource]
    names: list[Name]
