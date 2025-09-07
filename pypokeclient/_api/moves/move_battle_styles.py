"""Move Battle Styles endpoint."""

from pydantic.dataclasses import dataclass

from ..common_models import Name


@dataclass(frozen=True)
class MoveBattleStyle:
    id: int
    name: str
    names: list[Name]
