"""Moves endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import APIResource, MachineVersionDetail, Name, NamedAPIResource, VerboseEffect
from pypokeclient._api.pokemon.abilities import AbilityEffectChange


@dataclass(frozen=True)
class Move:
    id: int
    name: str
    accuracy: int
    effect_chance: int | None
    pp: int
    priority: int
    power: int
    contest_combos: ContestComboSets | None
    contest_type: NamedAPIResource | None
    contest_effect: APIResource | None
    damage_class: NamedAPIResource
    effect_entries: list[VerboseEffect]
    effect_changes: list[AbilityEffectChange]
    learned_by_pokemon: list[NamedAPIResource]
    flavor_text_entries: list[MoveFlavorText]
    generation: NamedAPIResource
    machines: list[MachineVersionDetail]
    meta: MoveMetaData | None
    names: list[Name]
    past_values: list[PastMoveStatValues]
    stat_changes: list[MoveStatChange]
    super_contest_effect: APIResource | None
    target: NamedAPIResource
    type: NamedAPIResource


@dataclass(frozen=True)
class ContestComboSets:
    normal: ContestComboDetail | None
    super: ContestComboDetail | None


@dataclass(frozen=True)
class ContestComboDetail:
    use_before: list[NamedAPIResource] | None
    use_after: list[NamedAPIResource] | None


@dataclass(frozen=True)
class MoveFlavorText:
    flavor_text: str
    language: NamedAPIResource
    version_group: NamedAPIResource


@dataclass(frozen=True)
class MoveMetaData:
    ailment: NamedAPIResource
    category: NamedAPIResource
    min_hits: int | None
    max_hits: int | None
    min_turns: int | None
    max_turns: int | None
    drain: int
    healing: int
    crit_rate: int
    ailment_chance: int
    flinch_chance: int
    stat_chance: int


@dataclass(frozen=True)
class MoveStatChange:
    change: int
    stat: NamedAPIResource


@dataclass(frozen=True)
class PastMoveStatValues:
    accuracy: int
    effect_chance: int
    power: int
    pp: int
    effect_entries: list[VerboseEffect]
    type: NamedAPIResource | None
    version_group: NamedAPIResource
