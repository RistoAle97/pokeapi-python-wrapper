"""Encounters Conditions endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class EncounterCondition:
    """Represent an encounter condition resource returned by PokéAPI.

    Encounter conditions affect which Pokémon can appear in the wild, for example, depending on the time of day.

    This model corresponds to the `https://pokeapi.co/api/v2/encounter-condition/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the encounter condition.
        name (str): The name of the encounter condition.
        names (list[Name]): The localized names of this encounter condition in different languages.
        values (list[NamedAPIResource]): The possible values of this encounter condition.
    """

    id: int
    name: str
    names: list[Name]
    values: list[NamedAPIResource]
