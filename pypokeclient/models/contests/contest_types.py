"""Contest Types endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import NamedAPIResource


@dataclass(frozen=True)
class ContestType:
    """Represent a contest type resource returned by PokéAPI.

    Contest types categorize Pokémon Contests according to the condition judged, such as Cool, Beauty, Cute, Smart, or
    Tough. Each contest type corresponds to a berry flavor.

    This model corresponds to the `https://pokeapi.co/api/v2/contest-type/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the contest type.
        name (str): The name of the contest type.
        berry_flavor (NamedAPIResource): The berry flavor associated with this contest type.
        names (list[ContestName]): The localized names of this contest type, including their associated colors and
            languages.
    """

    id: int
    name: str
    berry_flavor: NamedAPIResource
    names: list[ContestName]


@dataclass(frozen=True)
class ContestName:
    """Represent a localized name for a contest type.

    Attributes:
        name (str): The localized name of the contest type.
        color (str): The color associated with the contest type's name.
        language (NamedAPIResource): A reference to the language of this localized name.
    """

    name: str
    color: str
    language: NamedAPIResource
