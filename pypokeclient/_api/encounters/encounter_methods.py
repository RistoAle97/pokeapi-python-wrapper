"""Encounters Methods endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name


@dataclass(frozen=True)
class EncounterMethod:
    id: int
    name: str
    order: int
    names: list[Name]
