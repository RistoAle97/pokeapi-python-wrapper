"""Move Ailments endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class MoveAilment:
    """Represent a move ailment resource returned by PokéAPI.

    Move ailments are status conditions caused by moves used during battle.

    This model corresponds to the `/api/v2/move-ailment/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the move ailment.
        name (str): The name of the move ailment.
        moves (list[NamedAPIResource]): The moves that can cause this ailment.
        names (list[Name]): The localized names of this move ailment in different languages.
    """

    id: int
    name: str
    moves: list[NamedAPIResource]
    names: list[Name]
