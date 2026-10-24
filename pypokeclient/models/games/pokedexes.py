"""Pokedexes endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Description, Name, NamedAPIResource


@dataclass(frozen=True)
class Pokedex:
    """Represent a Pokédex resource returned by PokéAPI.

    Pokédexes catalogue Pokémon species and assign each species an entry number. They may cover an entire region, a
    portion of a region, or the National Pokédex.

    This model corresponds to the `/api/v2/pokedex/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the Pokédex.
        name (str): The name of the Pokédex.
        is_main_series (bool): Whether this Pokédex originated in the main series of the Pokémon video games.
        descriptions (list[Description]): The descriptions of this Pokédex in different languages.
        names (list[Name]): The localized names of this Pokédex in different languages.
        pokemon_entries (list[_PokemonEntry]): The Pokémon species catalogued in this Pokédex and their entry numbers.
        region (NamedAPIResource | None): The region this Pokédex catalogues Pokémon for, or `None` if no region is
            associated with it.
        version_groups (list[NamedAPIResource]): The version groups associated with this Pokédex.
    """

    id: int
    name: str
    is_main_series: bool
    descriptions: list[Description]
    names: list[Name]
    pokemon_entries: list[_PokemonEntry]
    region: NamedAPIResource | None
    version_groups: list[NamedAPIResource]


@dataclass(frozen=True)
class _PokemonEntry:
    """Represent a Pokémon species entry in a Pokédex.

    Attributes:
        entry_number (int): The index number assigned to this species within the Pokédex.
        pokemon_species (NamedAPIResource): A reference to the Pokémon species catalogued by this entry.
    """

    entry_number: int
    pokemon_species: NamedAPIResource
