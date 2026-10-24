"""Characteristics endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Description, NamedAPIResource


@dataclass(frozen=True)
class Characteristic:
    """Represent a characteristic resource returned by PokéAPI.

    Characteristics indicate the stat with the highest individual value (IV) of a Pokémon. Each characteristic is
    determined by the remainder of that IV divided by 5.

    This model corresponds to the `https://pokeapi.co/api/v2/characteristic/{id}/` endpoint.

    Attributes:
        id (int): The unique identifier of the characteristic.
        gene_modulo (int): The remainder of the highest individual value divided by 5.
        possible_values (list[int]): The possible individual values for the highest stat that correspond to this
            characteristic.
        highest_stat (NamedAPIResource): The stat associated with this characteristic.
        descriptions (list[Description]): The localized descriptions of this characteristic in different languages.
    """

    id: int
    gene_modulo: int
    possible_values: list[int]
    highest_stat: NamedAPIResource
    descriptions: list[Description]
