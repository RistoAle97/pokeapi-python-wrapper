"""Pokemon Shapes endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class PokemonShape:
    """Represent a Pokémon shape resource returned by PokéAPI.

    Pokémon shapes classify species by their physical silhouettes and are used to sort Pokémon in the Pokédex.

    This model corresponds to the `https://pokeapi.co/api/v2/pokemon-shape/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the Pokémon shape.
        name (str): The name of the Pokémon shape.
        awesome_names (list[AwesomeName]): The localized scientific or descriptive names associated with this Pokémon
            shape.
        names (list[Name]): The localized names of this Pokémon shape in different languages.
        pokemon_species (list[NamedAPIResource]): The Pokémon species that have this shape.
    """

    id: int
    name: str
    awesome_names: list[AwesomeName]
    names: list[Name]
    pokemon_species: list[NamedAPIResource]


@dataclass(frozen=True)
class AwesomeName:
    """Represent a localized scientific or descriptive name for a Pokémon shape.

    Attributes:
        awesome_name (str): The localized scientific or descriptive name.
        language (NamedAPIResource): The language in which the name is written.
    """

    awesome_name: str
    language: NamedAPIResource
