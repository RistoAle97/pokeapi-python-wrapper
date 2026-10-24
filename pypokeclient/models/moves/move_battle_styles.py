"""Move Battle Styles endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name


@dataclass(frozen=True)
class MoveBattleStyle:
    """Represent a move battle style resource returned by PokéAPI.

    Move battle styles describe how moves are used in the Battle Palace, where Pokémon choose moves according to their
    nature.

    This model corresponds to the `https://pokeapi.co/api/v2/move-battle-style/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the move battle style.
        name (str): The name of the move battle style.
        names (list[Name]): The localized names of this move battle style in different languages.
    """

    id: int
    name: str
    names: list[Name]
