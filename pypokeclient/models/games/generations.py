"""Generations endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class Generation:
    """Represent a generation resource returned by PokéAPI.

    Generations group Pokémon games according to the Pokémon, moves, abilities, and types available in each generation.

    This model corresponds to the `/api/v2/generation/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the generation.
        name (str): The name of the generation.
        abilities (list[NamedAPIResource]): The abilities introduced in this generation.
        names (list[Name]): The localized names of this generation in different languages.
        main_region (NamedAPIResource): The main region associated with this generation.
        moves (list[NamedAPIResource]): The moves introduced in this generation.
        pokemon_species (list[NamedAPIResource]): The Pokémon species introduced in this generation.
        types (list[NamedAPIResource]): The types introduced in this generation.
        version_groups (list[NamedAPIResource]): The version groups associated with this generation.
    """

    id: int
    name: str
    abilities: list[NamedAPIResource]
    names: list[Name]
    main_region: NamedAPIResource
    moves: list[NamedAPIResource]
    pokemon_species: list[NamedAPIResource]
    types: list[NamedAPIResource]
    version_groups: list[NamedAPIResource]
