"""Types endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import GenerationGameIndex, Name, NamedAPIResource


@dataclass(frozen=True)
class Type:
    """Represent a type resource returned by PokéAPI.

    Types determine the elemental properties of Pokémon and moves, including their damage effectiveness against other
    types.

    This model corresponds to the `/api/v2/type/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the type.
        name (str): The name of the type.
        damage_relations (TypeRelations): The damage effectiveness of this type against other types and its
            susceptibility to them.
        past_damage_relations (list[TypeRelationsPast]): The historical damage relations of this type across previous
            generations.
        game_indices (list[GenerationGameIndex]): The game indices assigned to this type in different generations.
        generation (NamedAPIResource): The generation in which this type was introduced.
        move_damage_class (NamedAPIResource): The damage class associated with this type.
        names (list[Name]): The localized names of this type in different languages.
        pokemon (list[TypePokemon]): The Pokémon that have this type, including the position of the type in their type
            list.
        moves (list[NamedAPIResource]): The moves that have this type.
        sprites (dict | None): Additional sprite data associated with this type, or `None` if no sprite data is
            available.
    """

    id: int
    name: str
    damage_relations: TypeRelations
    past_damage_relations: list[TypeRelationsPast]
    game_indices: list[GenerationGameIndex]
    generation: NamedAPIResource
    move_damage_class: NamedAPIResource
    names: list[Name]
    pokemon: list[TypePokemon]
    moves: list[NamedAPIResource]
    sprites: dict | None = None  # undocumented in PokéAPI docs


@dataclass(frozen=True)
class TypePokemon:
    """Represent a Pokémon that has a particular type.

    Attributes:
        slot (int): The position of this type in the Pokémon's type list.
        pokemon (NamedAPIResource): The Pokémon that has this type.
    """

    slot: int
    pokemon: NamedAPIResource


@dataclass(frozen=True)
class TypeRelations:
    """Represent the damage effectiveness of a type against other types.

    Attributes:
        no_damage_to (list[NamedAPIResource]): The types against which thistype deals no damage.
        half_damage_to (list[NamedAPIResource]): The types against which this type deals half damage.
        double_damage_to (list[NamedAPIResource]): The types against which this type deals double damage.
        no_damage_from (list[NamedAPIResource]): The types whose moves deal no damage to this type.
        half_damage_from (list[NamedAPIResource]): The types whose moves deal half damage to this type.
        double_damage_from (list[NamedAPIResource]): The types whose moves deal double damage to this type.
    """

    no_damage_to: list[NamedAPIResource]
    half_damage_to: list[NamedAPIResource]
    double_damage_to: list[NamedAPIResource]
    no_damage_from: list[NamedAPIResource]
    half_damage_from: list[NamedAPIResource]
    double_damage_from: list[NamedAPIResource]


@dataclass(frozen=True)
class TypeRelationsPast:
    """Represent historical damage relations for a type.

    Attributes:
        generation (NamedAPIResource): The last generation in which the listed damage relations applied.
        damage_relations (TypeRelations): The damage relations that applied up to and including the specified
            generation.
    """

    generation: NamedAPIResource
    damage_relations: TypeRelations
