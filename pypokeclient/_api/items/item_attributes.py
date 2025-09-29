"""Item Attributes endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Description, Name, NamedAPIResource


@dataclass(frozen=True)
class ItemAttribute:
    id: int
    name: str
    items: list[NamedAPIResource]
    names: list[Name]
    descriptions: list[Description]
