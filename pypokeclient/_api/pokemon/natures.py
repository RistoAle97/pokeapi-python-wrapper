"""Natures endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class Nature:
    id: int
    name: str
    decreased_stat: NamedAPIResource | None
    increased_stat: NamedAPIResource | None
    hates_flavor: NamedAPIResource | None
    likes_flavor: NamedAPIResource | None
    pokeathlon_stat_changes: list[NatureStatChange]
    move_battle_style_preferences: list[MoveBattleStylePreference]
    names: list[Name]


@dataclass(frozen=True)
class NatureStatChange:
    max_change: int
    pokeathlon_stat: NamedAPIResource


@dataclass(frozen=True)
class MoveBattleStylePreference:
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: NamedAPIResource
