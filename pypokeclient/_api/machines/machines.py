"""Machines endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import NamedAPIResource


@dataclass(frozen=True)
class Machine:
    id: int
    item: NamedAPIResource
    move: NamedAPIResource
    version_group: NamedAPIResource
