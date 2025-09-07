"""Encounters Methods endpoint."""

from pydantic.dataclasses import dataclass

from ..common_models import Name


@dataclass(frozen=True)
class EncounterMethod:
    id: int
    name: str
    order: int
    names: list[Name]
