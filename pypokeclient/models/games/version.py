"""Version endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class Version:
    """Represent a version resource returned by PokéAPI.

    Versions represent individual releases of the Pokémon games.

    This model corresponds to the `https://pokeapi.co/api/v2/version/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the version.
        name (str): The name of the version.
        names (list[Name]): The localized names of this version in different languages.
        version_group (NamedAPIResource): The version group to which this version belongs.
    """

    id: int
    name: str
    names: list[Name]
    version_group: NamedAPIResource
