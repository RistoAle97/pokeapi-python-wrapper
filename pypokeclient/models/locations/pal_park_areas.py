"""Pal Park Areas endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class PalParkArea:
    """Represent a Pal Park area resource returned by PokéAPI.

    Pal Park areas group Pokémon encounters according to specific habitats used in the Pal Park feature.

    This model corresponds to the `/api/v2/pal-park-area/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the Pal Park area.
        name (str): The name of the Pal Park area.
        names (list[Name]): The localized names of this Pal Park area in different languages.
        pokemon_encounters (list[PalParkEncounterSpecies]): The Pokémon species that can be encountered in this area,
            along with their encounter rates and base scores.
    """

    id: int
    name: str
    names: list[Name]
    pokemon_encounters: list[PalParkEncounterSpecies]


@dataclass(frozen=True)
class PalParkEncounterSpecies:
    """Represent a Pokémon species encountered in a Pal Park area.

    Attributes:
        base_score (int): The base score awarded for catching this Pokémon during a Pal Park run.
        rate (int): The base rate for encountering this Pokémon in the Pal Park area.
        pokemon_species (NamedAPIResource): A reference to the Pokémon species that can be encountered.
    """

    base_score: int
    rate: int
    pokemon_species: NamedAPIResource
