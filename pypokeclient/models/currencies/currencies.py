"""Currencies endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name


@dataclass(frozen=True)
class Currency:
    id: int
    name: str
    names: list[Name]
