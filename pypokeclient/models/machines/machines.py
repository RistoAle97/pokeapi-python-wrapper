"""Machines endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import NamedAPIResource


@dataclass(frozen=True)
class Machine:
    """Represent a machine resource returned by PokéAPI.

    Machines represent items that teach moves to Pokémon. Their associations with items and moves can vary between game
    version groups, so the same TM or HM may correspond to different machine resources across games.

    This model corresponds to the `https://pokeapi.co/api/v2/machine/{id}/` endpoint.

    Attributes:
        id (int): The unique identifier of the machine.
        item (NamedAPIResource): The TM or HM item associated with this machine.
        move (NamedAPIResource): The move taught by this machine.
        version_group (NamedAPIResource): The version group to which this machine applies.
    """

    id: int
    item: NamedAPIResource
    move: NamedAPIResource
    version_group: NamedAPIResource
