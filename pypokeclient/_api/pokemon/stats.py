"""Stats endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import APIResource, Name, NamedAPIResource


@dataclass(frozen=True)
class Stat:
    id: int
    name: str
    game_index: int
    is_battle_only: bool
    affecting_moves: MoveStatAffectSets
    affecting_natures: NatureStatAffectSets
    characteristics: list[APIResource]
    move_damage_class: NamedAPIResource | None
    names: list[Name]


@dataclass(frozen=True)
class MoveStatAffectSets:
    increase: list[MoveStatAffect]
    decrease: list[MoveStatAffect]


@dataclass(frozen=True)
class MoveStatAffect:
    change: int
    move: NamedAPIResource


@dataclass(frozen=True)
class NatureStatAffectSets:
    increase: list[NamedAPIResource]
    decrease: list[NamedAPIResource]
