"""Item Pockets endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class ItemPocket:
    id: int
    name: str
    categories: list[NamedAPIResource]
    names: list[Name]
