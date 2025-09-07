"""Machines endpoint."""

from pydantic.dataclasses import dataclass

from ..common_models import NamedAPIResource


@dataclass(frozen=True)
class Machine:
    id: int
    item: NamedAPIResource
    move: NamedAPIResource
    version_group: NamedAPIResource
