"""Encounter Condition Values endpoint."""

from pydantic.dataclasses import dataclass

from ..common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class EncounterConditionValue:
    id: int
    name: str
    order: int
    condition: NamedAPIResource
    names: list[Name]
