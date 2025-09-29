"""Item endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import (
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
    id: int
    name: str
    cost: int
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
    default: str | None


@dataclass(frozen=True)
class ItemHolderPokemon:
    pokemon: NamedAPIResource
    version_details: list[ItemHolderPokemonVersionDetail]


@dataclass(frozen=True)
class ItemHolderPokemonVersionDetail:
    rarity: int
    version: NamedAPIResource
