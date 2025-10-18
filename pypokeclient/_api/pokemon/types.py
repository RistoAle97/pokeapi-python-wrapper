"""Types endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import GenerationGameIndex, Name, NamedAPIResource


@dataclass(frozen=True)
class Type:
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
    slot: int
    pokemon: NamedAPIResource


@dataclass(frozen=True)
class TypeRelations:
    no_damage_to: list[NamedAPIResource]
    half_damage_to: list[NamedAPIResource]
    double_damage_to: list[NamedAPIResource]
    no_damage_from: list[NamedAPIResource]
    half_damage_from: list[NamedAPIResource]
    double_damage_from: list[NamedAPIResource]


@dataclass(frozen=True)
class TypeRelationsPast:
    generation: NamedAPIResource
    damage_relations: TypeRelations
