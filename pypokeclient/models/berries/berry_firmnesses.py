"""Berry Firmnesses endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class BerryFirmness:
    """Represent a berry firmness resource returned by PokéAPI.

    Berry firmnesses classify berries according to how soft or hard they are.

    This model corresponds to the `/api/v2/berry-firmness/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the berry firmness.
        name (str): The name of the berry firmness.
        berries (list[NamedAPIResource]): The berries that have this firmness.
        names (list[Name]): The names of this berry firmness in different languages.
    """

    id: int
    name: str
    berries: list[NamedAPIResource]
    names: list[Name]
