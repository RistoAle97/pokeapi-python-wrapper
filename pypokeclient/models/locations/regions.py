"""Regions endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class Region:
    """Represent a region resource returned by PokéAPI.

    Regions are organized areas of the Pokémon world. They group locations and are associated with Pokémon species,
    Pokédexes, and game versions.

    This model corresponds to the `https://pokeapi.co/api/v2/region/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the region.
        locations (list[NamedAPIResource]): The locations contained within this region.
        name (str): The name of the region.
        names (list[Name]): The localized names of this region in different languages.
        main_generation (NamedAPIResource | None): The generation in which this region was introduced, or `None` if no
            generation is associated with it.
        pokedexes (list[NamedAPIResource]): The Pokédexes that catalogue Pokémon in this region.
        version_groups (list[NamedAPIResource]): The version groups in which this region can be visited.
    """

    id: int
    locations: list[NamedAPIResource]
    name: str
    names: list[Name]
    main_generation: NamedAPIResource | None
    pokedexes: list[NamedAPIResource]
    version_groups: list[NamedAPIResource]
