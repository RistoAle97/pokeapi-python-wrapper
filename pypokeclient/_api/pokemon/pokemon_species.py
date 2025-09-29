"""Pokemon Species endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import APIResource, Description, FlavorText, Name, NamedAPIResource


@dataclass(frozen=True)
class PokemonSpecies:
    id: int
    name: str
    order: int
    gender_rate: int
    capture_rate: int
    base_happiness: int
    is_baby: bool
    is_legendary: bool
    is_mythical: bool
    hatch_counter: int
    has_gender_differences: bool
    forms_switchable: bool
    growth_rate: NamedAPIResource
    pokedex_numbers: list[PokemonSpeciesDexEntry]
    egg_groups: list[NamedAPIResource]
    color: NamedAPIResource
    shape: NamedAPIResource | None
    evolves_from_species: NamedAPIResource | None
    evolution_chain: APIResource
    habitat: NamedAPIResource | None
    generation: NamedAPIResource
    names: list[Name]
    pal_park_encounters: list[PalParkEncounterArea]
    flavor_text_entries: list[FlavorText]
    form_descriptions: list[Description]
    genera: list[Genus]
    varieties: list[PokemonSpeciesVariety]


@dataclass(frozen=True)
class Genus:
    genus: str
    language: NamedAPIResource


@dataclass(frozen=True)
class PokemonSpeciesDexEntry:
    entry_number: int
    pokedex: NamedAPIResource


@dataclass(frozen=True)
class PalParkEncounterArea:
    base_score: int
    rate: int
    area: NamedAPIResource


@dataclass(frozen=True)
class PokemonSpeciesVariety:
    is_default: bool
    pokemon: NamedAPIResource
