"""Pokemon Forms endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class PokemonForm:
    """Represent a Pokémon form resource returned by PokéAPI.

    Pokémon forms represent visually distinct forms of Pokémon, along with their types, sprites, and associated game
    versions.

    This model corresponds to the `https://pokeapi.co/api/v2/pokemon-form/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the Pokémon form.
        name (str): The name of the Pokémon form resource.
        order (int): The order used to sort this form among all Pokémon forms. Forms with equal order values are sorted
            by name.
        form_order (int): The order used to sort this form among the forms of the same Pokémon.
        is_default (bool): Whether this is the default form of the Pokémon.
        is_battle_only (bool): Whether this form can only occur during battle.
        is_mega (bool): Whether this form requires Mega Evolution.
        form_name (str): The name specific to this form.
        pokemon (NamedAPIResource): The Pokémon that can take this form.
        types (list[PokemonFormType]): The types associated with this form.
        sprites (PokemonFormSprites): The sprites used to depict this form.
        version_group (NamedAPIResource): The version group in which this form was introduced.
        names (list[Name]): The localized full names of this form, or an empty list if it has no specific full name.
        form_names (list[Name]): The localized names specific to this form, or an empty list if no specific form name
            is defined.
    """

    id: int
    name: str
    order: int
    form_order: int
    is_default: bool
    is_battle_only: bool
    is_mega: bool
    form_name: str
    pokemon: NamedAPIResource
    types: list[PokemonFormType]
    sprites: PokemonFormSprites
    version_group: NamedAPIResource
    names: list[Name]
    form_names: list[Name]


@dataclass(frozen=True)
class PokemonFormType:
    """Represent a type associated with a Pokémon form.

    Attributes:
        slot (int): The position of this type in the Pokémon form's type list.
        type (NamedAPIResource): The type associated with this form.
    """

    slot: int
    type: NamedAPIResource


@dataclass(frozen=True)
class PokemonFormSprites:
    """Represent the battle sprites associated with a Pokémon form.

    Attributes:
        front_default (str | None): The URL of the default front-facing sprite, or `None` if no sprite is available.
        front_shiny (str | None): The URL of the shiny front-facing sprite, or `None` if no sprite is available.
        back_default (str | None): The URL of the default back-facing sprite, or `None` if no sprite is available.
        back_shiny (str | None): The URL of the shiny back-facing sprite, or `None` if no sprite is available.
    """

    front_default: str | None
    front_shiny: str | None
    back_default: str | None
    back_shiny: str | None
