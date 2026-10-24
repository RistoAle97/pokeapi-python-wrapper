"""Item Categories endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class ItemCategory:
    """Represent an item category resource returned by PokéAPI.

    Item categories determine how items are organized in a player's bag.

    This model corresponds to the `/api/v2/item-category/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the item category.
        name (str): The name of the item category.
        items (list[NamedAPIResource]): The items belonging to this category.
        names (list[Name]): The localized names of this item category in different languages.
        pocket (NamedAPIResource): The item pocket in which items belonging to this category are stored.
    """

    id: int
    name: str
    items: list[NamedAPIResource]
    names: list[Name]
    pocket: NamedAPIResource
