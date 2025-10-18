"""Pokemon endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import NamedAPIResource, VersionGameIndex


@dataclass(frozen=True)
class Pokemon:
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
    sprites: PokemonSprite
    cries: PokemonCries
    species: NamedAPIResource
    stats: list[PokemonStat]
    types: list[PokemonType]


@dataclass(frozen=True)
class PokemonAbility:
    is_hidden: bool
    slot: int
    ability: NamedAPIResource | None


@dataclass(frozen=True)
class PokemonType:
    slot: int
    type: NamedAPIResource


@dataclass(frozen=True)
class PokemonTypePast:
    generation: NamedAPIResource
    types: list[PokemonType]


@dataclass(frozen=True)
class PokemonAbilityPast:
    generation: NamedAPIResource
    abilities: list[PokemonAbility]


@dataclass(frozen=True)
class PokemonHeldItem:
    item: NamedAPIResource
    version_details: list[PokemonHeldItemVersion]


@dataclass(frozen=True)
class PokemonHeldItemVersion:
    version: NamedAPIResource
    rarity: int


@dataclass(frozen=True)
class PokemonMove:
    move: NamedAPIResource
    version_group_details: list[PokemonMoveVersion]


@dataclass(frozen=True)
class PokemonMoveVersion:
    move_learn_method: NamedAPIResource
    version_group: NamedAPIResource
    level_learned_at: int
    order: int | None


@dataclass(frozen=True)
class PokemonStat:
    stat: NamedAPIResource
    effort: int
    base_stat: int


@dataclass(frozen=True)
class PokemonSprite:
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
    latest: str
    legacy: str | None
