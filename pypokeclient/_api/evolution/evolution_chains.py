"""Evolution Chains endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import NamedAPIResource


@dataclass(frozen=True)
class EvolutionChain:
    id: int
    baby_trigger_item: NamedAPIResource | None
    chain: ChainLink


@dataclass(frozen=True)
class ChainLink:
    is_baby: bool
    species: NamedAPIResource
    evolution_details: list[EvolutionDetail]
    evolves_to: list[ChainLink]


@dataclass(frozen=True)
class EvolutionDetail:
    item: NamedAPIResource | None
    trigger: NamedAPIResource
    gender: int | None
    held_item: NamedAPIResource | None
    known_move: NamedAPIResource | None
    known_move_type: NamedAPIResource | None
    location: NamedAPIResource | None
    min_level: int | None
    min_happiness: int | None
    min_beauty: int | None
    min_affection: int | None
    needs_overworld_rain: bool
    party_species: NamedAPIResource | None
    party_type: NamedAPIResource | None
    relative_physical_stats: int | None
    time_of_day: str
    trade_species: NamedAPIResource | None
    turn_upside_down: bool
