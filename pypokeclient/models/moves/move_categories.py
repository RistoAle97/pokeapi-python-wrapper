"""Move Categories endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Description, NamedAPIResource


@dataclass(frozen=True)
class MoveCategory:
    """Represent a move category resource returned by PokéAPI.

    Move categories group moves according to their general effects, such as dealing damage or inflicting status
    ailments.

    This model corresponds to the `https://pokeapi.co/api/v2/move-category/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the move category.
        name (str): The name of the move category.
        moves (list[NamedAPIResource]): The moves belonging to this category.
        descriptions (list[Description]): The localized descriptions of this move category in different languages.
    """

    id: int
    name: str
    moves: list[NamedAPIResource]
    descriptions: list[Description]
