"""Growth Rates endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Description, NamedAPIResource


@dataclass(frozen=True)
class GrowthRate:
    """Represent a growth rate resource returned by PokéAPI.

    Growth rates determine how quickly Pokémon gain experience and level up. Each growth rate defines a formula for
    calculating the experience required to reach each level.

    This model corresponds to the `https://pokeapi.co/api/v2/growth-rate/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the growth rate.
        name (str): The name of the growth rate.
        formula (str): The formula used to calculate the experience required for a Pokémon to reach a given level.
        descriptions (list[Description]): The localized descriptions of this growth rate in different languages.
        levels (list[GrowthRateExperienceLevel]): The experience required to reach each level under this growth rate.
        pokemon_species (list[NamedAPIResource]): The Pokémon species that use this growth rate.
    """

    id: int
    name: str
    formula: str
    descriptions: list[Description]
    levels: list[GrowthRateExperienceLevel]
    pokemon_species: list[NamedAPIResource]


@dataclass(frozen=True)
class GrowthRateExperienceLevel:
    """Represent the experience required to reach a level for a growth rate.

    Attributes:
        level (int): The Pokémon level associated with this experience requirement.
        experience (int): The total experience required to reach this level.
    """

    level: int
    experience: int
