"""Encounters Methods endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name


@dataclass(frozen=True)
class EncounterMethod:
    """Represent an encounter method resource returned by PokéAPI.

    Encounter methods describe how players can encounter wild Pokémon, such as walking through tall grass or exploring
    a cave.

    This model corresponds to the `https://pokeapi.co/api/v2/encounter-method/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the encounter method.
        name (str): The name of the encounter method.
        order (int): The value used to sort encounter methods.
        names (list[Name]): The localized names of this encounter method in different languages.
    """

    id: int
    name: str
    order: int
    names: list[Name]
