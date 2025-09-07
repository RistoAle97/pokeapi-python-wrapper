"""Encounters Conditions endpoint."""

from pydantic.dataclasses import dataclass

from ..common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class EncounterCondition:
    id: int
    name: str
    names: list[Name]
    values: list[NamedAPIResource]
