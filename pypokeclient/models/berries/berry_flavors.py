"""Berry Flavors endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class BerryFlavor:
    """Represent a berry flavor resource returned by the PokéAPI.

    Flavors determine whether a Pokémon benefits or suffers from eating a berry based on its nature.

    This model corresponds to the `/api/v2/berry-flavor/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the berry flavor.
        name (str): The name of the berry flavor.
        berries (list[FlavorBerryMap]): The berries associated with this flavor and the potency of the flavor for each
            berry.
        contest_type (NamedAPIResource): A reference to the contest type associated with this berry flavor.
        names (list[Name]): The names of this berry flavor in different languages.
    """

    id: int
    name: str
    berries: list[FlavorBerryMap]
    contest_type: NamedAPIResource
    names: list[Name]


@dataclass(frozen=True)
class FlavorBerryMap:
    """Represent a berry's potency for a particular flavor.

    Attributes:
        potency (int): How powerful this flavor is for the associated berry.
        berry (NamedAPIResource): A reference to the berry associated with this flavor potency.
    """

    potency: int
    berry: NamedAPIResource
