"""Move Learn Methods endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Description, Name, NamedAPIResource


@dataclass(frozen=True)
class MoveLearnMethod:
    id: int
    name: str
    descriptions: list[Description]
    names: list[Name]
    version_groups: list[NamedAPIResource]
