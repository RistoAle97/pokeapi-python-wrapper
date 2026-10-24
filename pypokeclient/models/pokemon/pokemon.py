"""Pokemon endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import NamedAPIResource, VersionGameIndex


@dataclass(frozen=True)
class Pokemon:
    """Represent a Pokémon resource returned by PokéAPI.

    Pokémon are individual creatures that belong to a Pokémon species. Different varieties of a species can have
    different stats, abilities, types, and forms.

    This model corresponds to the `https://pokeapi.co/api/v2/pokemon/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the Pokémon.
        name (str): The name of the Pokémon.
        base_experience (int): The base experience gained for defeating this Pokémon.
        height (int): The height of the Pokémon in decimeters.
        is_default (bool): Whether this is the default Pokémon variety for its species.
        order (int): The value used to sort Pokémon, approximately following National Pokédex order while grouping
            evolutionary families.
        weight (int): The weight of the Pokémon in hectograms.
        abilities (list[PokemonAbility]): The abilities this Pokémon can have, including its hidden abilities.
        forms (list[NamedAPIResource]): The forms this Pokémon can take.
        game_indices (list[VersionGameIndex]): The game indices assigned to this Pokémon in different game versions.
        held_items (list[PokemonHeldItem]): The items this Pokémon may hold when encountered, including
            version-specific details.
        location_area_encounters (str): The URL path for retrieving the location areas where this Pokémon can be
            encountered.
        moves (list[PokemonMove]): The moves this Pokémon can learn, including their learning methods and
            version-specific details.
        past_types (list[PokemonTypePast]): The historical types this Pokémon had in previous generations.
        past_abilities (list[PokemonAbilityPast]): The historical abilities this Pokémon had in previous generations.
        past_stats (list[PokemonStatPast]): The historical stats this Pokémon had in previous generations.
        sprites (PokemonSprite): The sprites used to depict this Pokémon.
        cries (PokemonCries): The audio recordings of this Pokémon's cries.
        species (NamedAPIResource): The species to which this Pokémon belongs.
        stats (list[PokemonStat]): The base stats and effort values associated with this Pokémon.
        types (list[PokemonType]): The types assigned to this Pokémon.
    """

    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: list[PokemonAbility]
    forms: list[NamedAPIResource]
    game_indices: list[VersionGameIndex]
    held_items: list[PokemonHeldItem]
    location_area_encounters: str
    moves: list[PokemonMove]
    past_types: list[PokemonTypePast]
    past_abilities: list[PokemonAbilityPast]
    past_stats: list[PokemonStatPast]
    sprites: PokemonSprite
    cries: PokemonCries
    species: NamedAPIResource
    stats: list[PokemonStat]
    types: list[PokemonType]


@dataclass(frozen=True)
class PokemonAbility:
    """Represent an ability slot associated with a Pokémon.

    Attributes:
        is_hidden (bool): Whether the ability is a hidden ability.
        slot (int): The slot occupied by this ability for the Pokémon.
        ability (NamedAPIResource | None): The ability assigned to this slot, or `None` if the slot was previously
            empty.
    """

    is_hidden: bool
    slot: int
    ability: NamedAPIResource | None


@dataclass(frozen=True)
class PokemonType:
    """Represent a type assigned to a Pokémon.

    Attributes:
        slot (int): The position of this type in the Pokémon's type list.
        type (NamedAPIResource): The type assigned to the Pokémon.
    """

    slot: int
    type: NamedAPIResource


@dataclass(frozen=True)
class PokemonTypePast:
    """Represent the historical types of a Pokémon.

    Attributes:
        generation (NamedAPIResource): The last generation in which the listed types applied to the Pokémon.
        types (list[PokemonType]): The types the Pokémon had up to and including the specified generation.
    """

    generation: NamedAPIResource
    types: list[PokemonType]


@dataclass(frozen=True)
class PokemonAbilityPast:
    """Represent the historical abilities of a Pokémon.

    Attributes:
        generation (NamedAPIResource): The last generation in which the listed abilities applied to the Pokémon.
        abilities (list[PokemonAbility]): The abilities the Pokémon had up to and including the specified generation.
            An entry with a `None` ability indicates a previously empty ability slot.
    """

    generation: NamedAPIResource
    abilities: list[PokemonAbility]


@dataclass(frozen=True)
class PokemonStatPast:
    """Represent the historical stats of a Pokémon.

    Attributes:
        generation (NamedAPIResource): The last generation in which the listed stats applied to the Pokémon.
        stats (list[PokemonStat]): The stats the Pokémon had up to and including the specified generation.
    """

    generation: NamedAPIResource
    stats: list[PokemonStat]


@dataclass(frozen=True)
class PokemonHeldItem:
    """Represent an item that a Pokémon may hold when encountered.

    Attributes:
        item (NamedAPIResource): The item that the Pokémon may hold.
        version_details (list[PokemonHeldItemVersion]): The game versions in which the Pokémon may hold this item and
            its holding rarity.
    """

    item: NamedAPIResource
    version_details: list[PokemonHeldItemVersion]


@dataclass(frozen=True)
class PokemonHeldItemVersion:
    """Represent version-specific details for an item held by a Pokémon.

    Attributes:
        version (NamedAPIResource): The game version in which the Pokémon may hold the item.
        rarity (int): How often the item is held, expressed as a percentage.
    """

    version: NamedAPIResource
    rarity: int


@dataclass(frozen=True)
class PokemonMove:
    """Represent a move that a Pokémon can learn.

    Attributes:
        move (NamedAPIResource): The move that the Pokémon can learn.
        version_group_details (list[PokemonMoveVersion]): The learning methods, levels, and version groups associated
            with this move.
    """

    move: NamedAPIResource
    version_group_details: list[PokemonMoveVersion]


@dataclass(frozen=True)
class PokemonMoveVersion:
    """Represent version-specific details about how a Pokémon learns a move.

    Attributes:
        move_learn_method (NamedAPIResource): The method used to learn the move, such as leveling up or using a
            machine.
        version_group (NamedAPIResource): The version group in which this learning method applies.
        level_learned_at (int): The minimum level at which the move can be learned through this method.
        order (int | None): The order used to determine move-learning or move-replacement priority, or `None` if no
            order is specified.
    """

    move_learn_method: NamedAPIResource
    version_group: NamedAPIResource
    level_learned_at: int
    order: int | None


@dataclass(frozen=True)
class PokemonStat:
    """Represent a stat and its associated values for a Pokémon.

    Attributes:
        stat (NamedAPIResource): The stat being described.
        effort (int): The effort points (EVs) awarded for defeating this Pokémon in this stat.
        base_stat (int): The base value of this stat for the Pokémon.
    """

    stat: NamedAPIResource
    effort: int
    base_stat: int


@dataclass(frozen=True)
class PokemonSprite:
    """Represent the sprites available for a Pokémon.

    Attributes:
        front_default (str | None): The URL of the default front-facing battle sprite, or `None` if unavailable.
        front_shiny (str | None): The URL of the shiny front-facing battle sprite, or `None` if unavailable.
        front_female (str | None): The URL of the female front-facing battle sprite, or `None` if unavailable.
        front_shiny_female (str | None): The URL of the shiny female front-facing battle sprite, or `None` if
            unavailable.
        back_default (str | None): The URL of the default back-facing battle sprite, or `None` if unavailable.
        back_shiny (str | None): The URL of the shiny back-facing battle sprite, or `None` if unavailable.
        back_female (str | None): The URL of the female back-facing battle sprite, or `None` if unavailable.
        back_shiny_female (str | None): The URL of the shiny female back-facing battle sprite, or `None` if
            unavailable.
        other (dict | None): Additional sprite collections, such as official artwork, Home sprites, and Dream World
            sprites, or `None` if unavailable.
        versions (dict | None): Sprite collections grouped by game generation and version, or `None` if unavailable.
    """

    front_default: str | None
    front_shiny: str | None
    front_female: str | None
    front_shiny_female: str | None
    back_default: str | None
    back_shiny: str | None
    back_female: str | None
    back_shiny_female: str | None
    other: dict | None = None  # undocumented in PokéAPI docs
    versions: dict | None = None  # undocumented in PokéAPI docs


@dataclass(frozen=True)
class PokemonCries:
    """Represent the cries available for a Pokémon.

    Attributes:
        latest (str | None): The URL of the latest recording of the Pokémon's cry, or `None` if unavailable.
        legacy (str | None): The URL of the legacy recording of the Pokémon's cry, or `None` if unavailable.
    """

    latest: str | None
    legacy: str | None
