"""Item Attributes endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Description, Name, NamedAPIResource


@dataclass(frozen=True)
class ItemAttribute:
    """Represent an item attribute resource returned by PokéAPI.

    Item attributes describe particular properties of items, such as whether they can be used in battle or consumed.

    This model corresponds to the `https://pokeapi.co/api/v2/item-attribute/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the item attribute.
        name (str): The name of the item attribute.
        items (list[NamedAPIResource]): The items that have this attribute.
        names (list[Name]): The localized names of this item attribute in different languages.
        descriptions (list[Description]): The localized descriptions of this item attribute in different languages.
    """

    id: int
    name: str
    items: list[NamedAPIResource]
    names: list[Name]
    descriptions: list[Description]
