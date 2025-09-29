"""Pokeathlon Stats endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class PokeathlonStat:
    id: int
    name: str
    names: list[Name]
    affecting_natures: NaturePokeathlonStatAffectSets


@dataclass(frozen=True)
class NaturePokeathlonStatAffectSets:
    increase: list[NaturePokeathlonStatAffect]
    decrease: list[NaturePokeathlonStatAffect]


@dataclass(frozen=True)
class NaturePokeathlonStatAffect:
    max_change: int
    nature: NamedAPIResource
