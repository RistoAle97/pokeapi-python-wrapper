"""Locations endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import GenerationGameIndex, Name, NamedAPIResource


@dataclass(frozen=True)
class Location:
    """Represent a location resource returned by PokéAPI.

    Locations represent places that can be visited in the Pokémon games, such as cities and routes, and belong to
    regions of the Pokémon world.

    This model corresponds to the `https://pokeapi.co/api/v2/location/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the location.
        name (str): The name of the location.
        region (NamedAPIResource | None): The region containing this location, or `None` if no region is associated
            with it.
        names (list[Name]): The localized names of this location in different languages.
        game_indices (list[GenerationGameIndex]): The indices identifying this location in different game generations.
        areas (list[NamedAPIResource]): The location areas contained within this location.
    """

    id: int
    name: str
    region: NamedAPIResource | None
    names: list[Name]
    game_indices: list[GenerationGameIndex]
    areas: list[NamedAPIResource]
