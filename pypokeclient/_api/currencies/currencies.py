"""Currencies endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name


@dataclass(frozen=True)
class Currency:
    id: int
    name: str
    names: list[Name]
