"""Pokemon Forms endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class PokemonForm:
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
    slot: int
    type: NamedAPIResource


@dataclass(frozen=True)
class PokemonFormSprites:
    front_default: str
    front_shiny: str
    back_default: str
    back_shiny: str
