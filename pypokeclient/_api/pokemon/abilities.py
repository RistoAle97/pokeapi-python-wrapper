"""Abilities endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Effect, Name, NamedAPIResource, VerboseEffect


@dataclass(frozen=True)
class Ability:
    id: int
    name: str
    is_main_series: bool
    generation: NamedAPIResource
    names: list[Name]
    effect_entries: list[VerboseEffect]
    effect_changes: list[AbilityEffectChange]
    flavor_text_entries: list[AbilityFlavorText]
    pokemon: list[AbilityPokemon]


@dataclass(frozen=True)
class AbilityEffectChange:
    effect_entries: list[Effect]
    version_group: NamedAPIResource


@dataclass(frozen=True)
class AbilityFlavorText:
    flavor_text: str
    language: NamedAPIResource
    version_group: NamedAPIResource


@dataclass(frozen=True)
class AbilityPokemon:
    is_hidden: bool
    slot: int
    pokemon: NamedAPIResource
