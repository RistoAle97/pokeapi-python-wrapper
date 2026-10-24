"""Evolution Trigger endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class EvolutionTrigger:
    """Represent an evolution trigger resource returned by PokéAPI.

    Evolution triggers describe the events that cause Pokémon to evolve, such as leveling up, using an item, or
    trading.

    This model corresponds to the `/api/v2/evolution-trigger/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the evolution trigger.
        name (str): The name of the evolution trigger.
        names (list[Name]): The localized names of this evolution trigger in different languages.
        pokemon_species (list[NamedAPIResource]): The Pokémon species that result from this evolution trigger.
    """

    id: int
    name: str
    names: list[Name]
    pokemon_species: list[NamedAPIResource]
