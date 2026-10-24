"""Currencies endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name


@dataclass(frozen=True)
class Currency:
    """Represent a currency resource returned by PokéAPI.

    Currencies are forms of money used throughout the Pokémon games to purchase items and services and participate in
    various game mechanics.

    This model corresponds to the `https://pokeapi.co/api/v2/currency/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the currency.
        name (str): The name of the currency.
        names (list[Name]): The names of this currency in different languages.
    """

    id: int
    name: str
    names: list[Name]
