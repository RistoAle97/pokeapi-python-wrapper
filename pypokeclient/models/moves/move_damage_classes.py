"""Move Damage Classes endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Description, Name, NamedAPIResource


@dataclass(frozen=True)
class MoveDamageClass:
    """Represent a move damage class resource returned by PokéAPI.

    Move damage classes categorize moves as physical, special, or status, indicating whether they deal physical damage,
    special damage, or no direct damage.

    This model corresponds to the `https://pokeapi.co/api/v2/move-damage-class/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the move damage class.
        name (str): The name of the move damage class.
        descriptions (list[Description]): The localized descriptions of this move damage class in different languages.
        moves (list[NamedAPIResource]): The moves belonging to this damage class.
        names (list[Name]): The localized names of this move damage class in different languages.
    """

    id: int
    name: str
    descriptions: list[Description]
    moves: list[NamedAPIResource]
    names: list[Name]
