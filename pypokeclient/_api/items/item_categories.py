"""Item Categories endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class ItemCategory:
    id: int
    name: str
    items: list[NamedAPIResource]
    names: list[Name]
    pocket: NamedAPIResource
