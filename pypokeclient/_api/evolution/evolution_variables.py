"""Evolution Variables endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Description, Name, NamedAPIResource


@dataclass(frozen=True)
class EvolutionVariable:
    id: int
    name: str
    symbol: str
    data_type: str
    version_group: NamedAPIResource
    names: list[Name]
    descriptions: list[Description]
