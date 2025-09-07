"""Berry Firmnesses endpoint."""

from pydantic.dataclasses import dataclass

from ..common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class BerryFirmness:
    id: int
    name: str
    berries: list[NamedAPIResource]
    names: list[Name]
