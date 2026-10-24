"""Move Targets endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Description, Name, NamedAPIResource


@dataclass(frozen=True)
class MoveTarget:
    """Represent a move target resource returned by PokéAPI.

    Move targets describe the entities or areas that moves can affect during battle, such as a specific Pokémon, all
    opposing Pokémon, the battlefield, or another move.

    This model corresponds to the `/api/v2/move-target/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the move target.
        name (str): The name of the move target.
        descriptions (list[Description]): The localized descriptions of this move target in different languages.
        moves (list[NamedAPIResource]): The moves directed at this target.
        names (list[Name]): The localized names of this move target in different languages.
    """

    id: int
    name: str
    descriptions: list[Description]
    moves: list[NamedAPIResource]
    names: list[Name]
