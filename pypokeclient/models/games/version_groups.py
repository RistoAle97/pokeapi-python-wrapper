"""Version Groups endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import NamedAPIResource


@dataclass(frozen=True)
class VersionGroup:
    """Represent a version group resource returned by PokéAPI.

    Version groups categorize closely related Pokémon game versions and group information about their generations,
    regions, Pokédexes, and move-learning methods.

    This model corresponds to the `https://pokeapi.co/api/v2/version-group/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the version group.
        name (str): The name of the version group.
        order (int): The value used to sort version groups, approximately by release date, with similar versions
            grouped together.
        generation (NamedAPIResource): The generation in which this version group was introduced.
        move_learn_methods (list[NamedAPIResource]): The methods by which Pokémon can learn moves in this version
            group.
        pokedexes (list[NamedAPIResource]): The Pokédexes introduced in this version group.
        regions (list[NamedAPIResource]): The regions that can be visited in this version group.
        versions (list[NamedAPIResource]): The game versions belonging to this version group.
    """

    id: int
    name: str
    order: int
    generation: NamedAPIResource
    move_learn_methods: list[NamedAPIResource]
    pokedexes: list[NamedAPIResource]
    regions: list[NamedAPIResource]
    versions: list[NamedAPIResource]
