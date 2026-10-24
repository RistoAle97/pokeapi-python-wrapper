"""Location Areas endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource, VersionEncounterDetail


@dataclass(frozen=True)
class LocationArea:
    """Represent a location area resource returned by PokéAPI.

    Location areas represent sections of locations, such as floors in a building or cave. Each area defines the Pokémon
    that can be encountered there and the methods used to encounter them.

    This model corresponds to the `https://pokeapi.co/api/v2/location-area/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the location area.
        name (str): The name of the location area.
        game_index (int): The internal identifier of this resource within the game data.
        encounter_method_rates (list[EncounterMethodRate]): The encounter methods available in this area and their
            rates for different game versions.
        location (NamedAPIResource): The location that contains this area.
        names (list[Name]): The localized names of this location area in different languages.
        pokemon_encounters (list[PokemonEncounter]): The Pokémon that can be encountered in this area and their
            version-specific details.
    """

    id: int
    name: str
    game_index: int
    encounter_method_rates: list[EncounterMethodRate]
    location: NamedAPIResource
    names: list[Name]
    pokemon_encounters: list[PokemonEncounter]


@dataclass(frozen=True)
class EncounterMethodRate:
    """Represent an encounter method and its rates in different game versions.

    Attributes:
        encounter_method (NamedAPIResource): The method used to encounter Pokémon in this location area.
        version_details (list[EncounterVersionDetails]): The encounter rates associated with this method across
            different game versions.
    """

    encounter_method: NamedAPIResource
    version_details: list[EncounterVersionDetails]


@dataclass(frozen=True)
class EncounterVersionDetails:
    """Represent an encounter rate for a specific game version.

    Attributes:
        rate (int): The chance of an encounter occurring with this method in the specified game version.
        version (NamedAPIResource): The game version to which this rate applies.
    """

    rate: int
    version: NamedAPIResource


@dataclass(frozen=True)
class PokemonEncounter:
    """Represent a Pokémon that can be encountered in a location area.

    Attributes:
        pokemon (NamedAPIResource): The Pokémon that can be encountered.
        version_details (list[VersionEncounterDetail]): The game versions and encounter details associated with this
            Pokémon.
    """

    pokemon: NamedAPIResource
    version_details: list[VersionEncounterDetail]
