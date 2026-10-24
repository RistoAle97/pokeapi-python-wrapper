"""Pokemon Colors endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class PokemonColor:
    """Represent a Pokémon color resource returned by PokéAPI.

    Pokémon colors are used to sort Pokémon species in the Pokédex according to the color that is most apparent or
    covers most of their bodies.

    This model corresponds to the `/api/v2/pokemon-color/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the Pokémon color.
        name (str): The name of the Pokémon color.
        names (list[Name]): The localized names of this Pokémon color in different languages.
        pokemon_species (list[NamedAPIResource]): The Pokémon species associated with this color.
    """

    id: int
    name: str
    names: list[Name]
    pokemon_species: list[NamedAPIResource]
