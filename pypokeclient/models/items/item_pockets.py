"""Item Pockets endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class ItemPocket:
    """Represent an item pocket resource returned by PokéAPI.

    Item pockets organize categories of items in a player's bag.

    This model corresponds to the `https://pokeapi.co/api/v2/item-pocket/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the item pocket.
        name (str): The name of the item pocket.
        categories (list[NamedAPIResource]): The item categories associated with this pocket.
        names (list[Name]): The localized names of this item pocket in different languages.
    """

    id: int
    name: str
    categories: list[NamedAPIResource]
    names: list[Name]
