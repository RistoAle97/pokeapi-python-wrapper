"""Item endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import (
    APIResource,
    GenerationGameIndex,
    MachineVersionDetail,
    Name,
    NamedAPIResource,
    VerboseEffect,
    VersionGroupFlavorText,
)


@dataclass(frozen=True)
class Item:
    """Represent an item resource returned by PokéAPI.

    Items are objects that players can collect, store in their bag, and use throughout the Pokémon games for purposes
    such as healing Pokémon, catching wild Pokémon, powering up Pokémon, and accessing new areas.

    This model corresponds to the `https://pokeapi.co/api/v2/item/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the item.
        name (str): The name of the item.
        prices (list[ItemPrice]): The purchase and sell prices of this item across different version groups and
            currencies.
        fling_power (int | None): The power of the move Fling when used with this item, or `None` if no power is
            defined.
        fling_effect (NamedAPIResource | None): The effect produced when Fling is used with this item, or `None` if no
            effect is defined.
        attributes (list[NamedAPIResource]): The attributes associated with this item.
        category (NamedAPIResource): The category to which this item belongs.
        effect_entries (list[VerboseEffect]): The descriptions of this item's effects in different languages.
        flavor_text_entries (list[VersionGroupFlavorText]): The flavor text descriptions of this item across different
            game versions.
        game_indices (list[GenerationGameIndex]): The indices identifying this item in different generations.
        names (list[Name]): The localized names of this item in different languages.
        sprites (ItemSprites | None): The sprites used to depict this item in the games, or `None` if no sprite data
            is available.
        held_by_pokemon (list[ItemHolderPokemon]): The Pokémon that may be found holding this item, including their
            version-specific details.
        baby_trigger_for (APIResource | None): The evolution chain associated with producing a baby Pokémon during
            breeding using this item, or `None` if no such chain is defined.
        machines (list[MachineVersionDetail]): The machines associated with this item across different version groups.
    """

    id: int
    name: str
    prices: list[ItemPrice]
    fling_power: int | None
    fling_effect: NamedAPIResource | None
    attributes: list[NamedAPIResource]
    category: NamedAPIResource
    effect_entries: list[VerboseEffect]
    flavor_text_entries: list[VersionGroupFlavorText]
    game_indices: list[GenerationGameIndex]
    names: list[Name]
    sprites: ItemSprites | None
    held_by_pokemon: list[ItemHolderPokemon]
    baby_trigger_for: APIResource | None
    machines: list[MachineVersionDetail]


@dataclass(frozen=True)
class ItemSprites:
    """Represent the sprite data associated with an item.

    Attributes:
        default (str | None): The URL of the default sprite for this item, or `None` if no sprite is available.
    """

    default: str | None


@dataclass(frozen=True)
class ItemHolderPokemon:
    """Represent a Pokémon that may hold an item.

    Attributes:
        pokemon (NamedAPIResource): A reference to the Pokémon species that may hold this item.
        version_details (list[ItemHolderPokemonVersionDetail]): The version-specific details describing this
            Pokémon's possession of the item.
    """

    pokemon: NamedAPIResource
    version_details: list[ItemHolderPokemonVersionDetail]


@dataclass(frozen=True)
class ItemHolderPokemonVersionDetail:
    """Represent version-specific details about an item held by a Pokémon.

    Attributes:
        rarity (int): The chance of finding this item held by the Pokémon, expressed as a percentage.
        version (NamedAPIResource): The game version to which this detail applies.
    """

    rarity: int
    version: NamedAPIResource


@dataclass(frozen=True)
class ItemPrice:
    """Represent an item's purchase and sell prices for a version group.

    Attributes:
        currency (NamedAPIResource): The currency used for these prices.
        purchase_price (int | None): The price required to purchase the item, or `None` if the item cannot be
            purchased.
        sell_price (int | None): The price received when selling the item, or `None` if the item cannot be sold.
        version_group (NamedAPIResource): The version group to which these prices apply.
    """

    currency: NamedAPIResource
    purchase_price: int | None
    sell_price: int | None
    version_group: NamedAPIResource
