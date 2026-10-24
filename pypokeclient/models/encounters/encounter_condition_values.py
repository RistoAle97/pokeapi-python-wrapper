"""Encounter Condition Values endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class EncounterConditionValue:
    """Represent an encounter condition value resource returned by PokéAPI.

    Encounter condition values represent the possible states of an encounter condition that affect which Pokémon can
    appear in the wild, such as whether it is day or night.

    This model corresponds to the `/api/v2/encounter-condition-value/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the encounter condition value.
        name (str): The name of the encounter condition value.
        condition (NamedAPIResource): The encounter condition this value belongs to.
        names (list[Name]): The localized names of this encounter condition value in different languages.
    """

    id: int
    name: str
    condition: NamedAPIResource
    names: list[Name]
