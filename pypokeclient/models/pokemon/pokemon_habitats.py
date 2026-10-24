"""Pokemon Habitats endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class PokemonHabitat:
    """Represent a Pokémon habitat resource returned by PokéAPI.

    Habitats describe the types of terrain where Pokémon can be found and may also identify areas associated with rare
    or legendary Pokémon.

    This model corresponds to the `https://pokeapi.co/api/v2/pokemon-habitat/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the Pokémon habitat.
        name (str): The name of the Pokémon habitat.
        names (list[Name]): The localized names of this Pokémon habitat in different languages.
        pokemon_species (list[NamedAPIResource]): The Pokémon species that can be found in this habitat.
    """

    id: int
    name: str
    names: list[Name]
    pokemon_species: list[NamedAPIResource]
