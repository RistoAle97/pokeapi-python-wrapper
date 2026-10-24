"""Pokeathlon Stats endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class PokeathlonStat:
    """Represent a Pokéathlon stat resource returned by PokéAPI.

    Pokéathlon stats measure different aspects of a Pokémon's performance in Pokéathlon competitions.

    This model corresponds to the `/api/v2/pokeathlon-stat/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the Pokéathlon stat.
        name (str): The name of the Pokéathlon stat.
        names (list[Name]): The localized names of this Pokéathlon stat in different languages.
        affecting_natures (NaturePokeathlonStatAffectSets): The natures that increase or decrease this Pokéathlon stat
            and the amount of change.
    """

    id: int
    name: str
    names: list[Name]
    affecting_natures: NaturePokeathlonStatAffectSets


@dataclass(frozen=True)
class NaturePokeathlonStatAffectSets:
    """Represent the effects of natures on a Pokéathlon stat.

    Attributes:
        increase (list[NaturePokeathlonStatAffect]): The natures that increase this Pokéathlon stat and their maximum
            changes.
        decrease (list[NaturePokeathlonStatAffect]): The natures that decrease this Pokéathlon stat and their maximum
            changes.
    """

    increase: list[NaturePokeathlonStatAffect]
    decrease: list[NaturePokeathlonStatAffect]


@dataclass(frozen=True)
class NaturePokeathlonStatAffect:
    """Represent the effect of a nature on a Pokéathlon stat.

    Attributes:
        max_change (int): The maximum amount by which the nature changes the Pokéathlon stat.
        nature (NamedAPIResource): The nature responsible for the change.
    """

    max_change: int
    nature: NamedAPIResource
