"""Base models shared by the endpoints."""

from __future__ import annotations

from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class APIResource:
    url: str


@dataclass(frozen=True)
class Description:
    description: str
    language: NamedAPIResource


@dataclass(frozen=True)
class Effect:
    effect: str
    language: NamedAPIResource


@dataclass(frozen=True)
class Encounter:
    min_level: int
    max_level: int
    condition_values: list[NamedAPIResource]
    chance: int
    method: NamedAPIResource


@dataclass(frozen=True)
class FlavorText:
    flavor_text: str
    language: NamedAPIResource
    version: NamedAPIResource | None = None


@dataclass(frozen=True)
class GenerationGameIndex:
    game_index: int
    generation: NamedAPIResource


@dataclass(frozen=True)
class MachineVersionDetail:
    machine: APIResource
    version_group: NamedAPIResource


@dataclass(frozen=True)
class Name:
    name: str
    language: NamedAPIResource


@dataclass(frozen=True)
class NamedAPIResource:
    name: str
    url: str


@dataclass(frozen=True)
class VerboseEffect:
    effect: str
    short_effect: str
    language: NamedAPIResource


@dataclass(frozen=True)
class VersionEncounterDetail:
    version: NamedAPIResource
    max_chance: int
    encounter_details: list[Encounter]


@dataclass(frozen=True)
class VersionGameIndex:
    game_index: int
    version: NamedAPIResource


@dataclass(frozen=True)
class VersionGroupFlavorText:
    text: str
    language: NamedAPIResource
    version_group: NamedAPIResource
