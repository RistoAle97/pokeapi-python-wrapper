"""Evolution Variables endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Description, Name, NamedAPIResource


@dataclass(frozen=True)
class EvolutionVariable:
    """Represent an evolution variable resource returned by PokéAPI.

    Evolution variables represent parameters used in boolean expressions for form-branching evolutions. They can
    describe values stored on a Pokémon or inputs provided by the player during an evolution.

    This model corresponds to the `https://pokeapi.co/api/v2/evolution-variable/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the evolution variable.
        name (str): The name of the evolution variable.
        symbol (str): The symbol used to represent this variable in evolution condition expressions.
        data_type (str): The data type of the evolution variable.
        source (str): Where the variable's value comes from: `pokemon` for data stored on the Pokémon, or
            `player-input` for player actions performed during evolution.
        version_group (NamedAPIResource): The version group in which this evolution variable was introduced.
        names (list[Name]): The localized names of this evolution variable in different languages.
        descriptions (list[Description]): The localized descriptions of this evolution variable in different languages.
    """

    id: int
    name: str
    symbol: str
    data_type: str
    source: str
    version_group: NamedAPIResource
    names: list[Name]
    descriptions: list[Description]
