"""Move Categories endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Description, NamedAPIResource


@dataclass(frozen=True)
class MoveCategory:
    id: int
    name: str
    moves: list[NamedAPIResource]
    descriptions: list[Description]
