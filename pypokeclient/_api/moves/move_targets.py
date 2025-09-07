"""Move Targets endpoint."""

from pydantic.dataclasses import dataclass

from ..common_models import Description, Name, NamedAPIResource


@dataclass(frozen=True)
class MoveTarget:
    id: int
    name: str
    descriptions: list[Description]
    moves: list[NamedAPIResource]
    names: list[Name]
