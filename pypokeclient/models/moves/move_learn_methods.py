"""Move Learn Methods endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Description, Name, NamedAPIResource


@dataclass(frozen=True)
class MoveLearnMethod:
    """Represent a move learn method resource returned by PokéAPI.

    Move learn methods describe how Pokémon learn moves, such as by leveling up, using a machine, breeding, or being
    taught by a move tutor.

    This model corresponds to the `/api/v2/move-learn-method/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the move learn method.
        name (str): The name of the move learn method.
        descriptions (list[Description]): The localized descriptions of this move learn method in different languages.
        names (list[Name]): The localized names of this move learn method in different languages.
        version_groups (list[NamedAPIResource]): The version groups in which Pokémon can learn moves through this
            method.
    """

    id: int
    name: str
    descriptions: list[Description]
    names: list[Name]
    version_groups: list[NamedAPIResource]
