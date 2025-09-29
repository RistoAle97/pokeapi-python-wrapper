"""Encounter Condition Values endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class EncounterConditionValue:
    id: int
    name: str
    condition: NamedAPIResource
    names: list[Name]
