"""Stats endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import APIResource, Name, NamedAPIResource


@dataclass(frozen=True)
class Stat:
    """Represent a stat resource returned by PokéAPI.

    Stats determine certain aspects of Pokémon performance in battle. Their values grow as Pokémon gain levels and can
    be temporarily altered by battle effects.

    This model corresponds to the `https://pokeapi.co/api/v2/stat/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the stat.
        name (str): The name of the stat.
        game_index (int): The identifier used for this stat in the games.
        is_battle_only (bool): Whether this stat only exists during battle.
        affecting_items (list[NamedAPIResource]): The items that affect this stat.
        affecting_moves (MoveStatAffectSets): The moves that increase or decrease this stat and the magnitude of their
            effects.
        affecting_natures (NatureStatAffectSets): The natures that increase or decrease this stat.
        characteristics (list[APIResource]): The characteristics associated with Pokémon whose highest base stat is
            this stat.
        move_damage_class (NamedAPIResource | None): The damage class directly associated with this stat, or `None` if
            no class is associated.
        names (list[Name]): The localized names of this stat in different languages.
    """

    id: int
    name: str
    game_index: int
    is_battle_only: bool
    affecting_items: list[NamedAPIResource]
    affecting_moves: MoveStatAffectSets
    affecting_natures: NatureStatAffectSets
    characteristics: list[APIResource]
    move_damage_class: NamedAPIResource | None
    names: list[Name]


@dataclass(frozen=True)
class MoveStatAffectSets:
    """Represent the moves that increase or decrease a stat.

    Attributes:
        increase (list[MoveStatAffect]): The moves that increase the stat and the magnitude of their effects.
        decrease (list[MoveStatAffect]): The moves that decrease the stat and the magnitude of their effects.
    """

    increase: list[MoveStatAffect]
    decrease: list[MoveStatAffect]


@dataclass(frozen=True)
class MoveStatAffect:
    """Represent the effect of a move on a stat.

    Attributes:
        change (int): The maximum amount by which the move changes the stat.
        move (NamedAPIResource): The move that causes the change.
    """

    change: int
    move: NamedAPIResource


@dataclass(frozen=True)
class NatureStatAffectSets:
    """Represent the natures that increase or decrease a stat.

    Attributes:
        increase (list[NamedAPIResource]): The natures that increase the stat.
        decrease (list[NamedAPIResource]): The natures that decrease the stat.
    """

    increase: list[NamedAPIResource]
    decrease: list[NamedAPIResource]
