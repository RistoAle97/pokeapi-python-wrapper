"""Genders endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import NamedAPIResource


@dataclass(frozen=True)
class Gender:
    """Represent a gender resource returned by PokéAPI.

    Genders describe the sex categories of Pokémon, which can affect breeding, visual differences, and certain
    evolutionary paths.

    This model corresponds to the `https://pokeapi.co/api/v2/gender/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the gender.
        name (str): The name of the gender.
        pokemon_species_details (list[PokemonSpeciesGender]): The Pokémon species associated with this gender and their
            gender ratios.
        required_for_evolution (list[NamedAPIResource]): The Pokémon species that require this gender for a Pokémon to
            evolve into them.
    """

    id: int
    name: str
    pokemon_species_details: list[PokemonSpeciesGender]
    required_for_evolution: list[NamedAPIResource]


@dataclass(frozen=True)
class PokemonSpeciesGender:
    """Represent gender ratio information for a Pokémon species.

    Attributes:
        rate (int): The chance of the Pokémon being female, expressed in eighths, or -1 if the species is genderless.
        pokemon_species (NamedAPIResource): A reference to the Pokémon species associated with this gender ratio.
    """

    rate: int
    pokemon_species: NamedAPIResource
