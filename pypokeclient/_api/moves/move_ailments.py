"""Move Ailments endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class MoveAilment:
    id: int
    name: str
    moves: list[NamedAPIResource]
    names: list[Name]
