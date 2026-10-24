"""Egg Groups endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class EggGroup:
    """Represent an egg group resource returned by PokéAPI.

    Egg groups classify Pokémon species according to their breeding compatibility. A Pokémon species may belong to one
    or two egg groups.

    This model corresponds to the `https://pokeapi.co/api/v2/egg-group/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the egg group.
        name (str): The name of the egg group.
        names (list[Name]): The localized names of this egg group in different languages.
        pokemon_species (list[NamedAPIResource]): The Pokémon species that belong to this egg group.
    """

    id: int
    name: str
    names: list[Name]
    pokemon_species: list[NamedAPIResource]
