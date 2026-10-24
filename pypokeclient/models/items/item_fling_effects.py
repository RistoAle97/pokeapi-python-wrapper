"""Item Fling Effects endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Effect, NamedAPIResource


@dataclass(frozen=True)
class ItemFlingEffect:
    """Represent an item fling effect resource returned by PokéAPI.

    Item fling effects describe the effects produced when the move Fling is used with different items.

    This model corresponds to the `https://pokeapi.co/api/v2/item-fling-effect/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the item fling effect.
        name (str): The name of the item fling effect.
        effect_entries (list[Effect]): The descriptions of this fling effect in different languages.
        items (list[NamedAPIResource]): The items that have this fling effect.
    """

    id: int
    name: str
    effect_entries: list[Effect]
    items: list[NamedAPIResource]
