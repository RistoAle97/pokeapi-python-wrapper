"""Characteristics endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Description, NamedAPIResource


@dataclass(frozen=True)
class Characteristic:
    id: int
    gene_modulo: int
    possible_values: list[int]
    highest_stat: NamedAPIResource
    descriptions: list[Description]
