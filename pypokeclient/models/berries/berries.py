"""Berries endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import NamedAPIResource


@dataclass(frozen=True)
class Berry:
    """Represent a berry resource returned by PokéAPI.

    Berries are small fruits that can restore HP, cure status conditions,
    enhance stats, or negate damage when consumed by Pokémon.

    This model corresponds to the `https://pokeapi.co/api/v2/berry/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the berry.
        name (str): The name of the berry.
        growth_time (int | None): The time, in hours, required for the berry tree to advance through one growth stage.
            A tree passes through four stages before its berries can be harvested.
        max_harvest (int | None): The maximum number of berries that can grow on a single tree in Generation IV.
        natural_gift_power (int | None): The power of the move Natural Gift when used with this berry.
        size (int | None): The size of the berry, in millimeters.
        smoothness (int | None): The smoothness of the berry, used when making
            Pokéblocks or Poffins.
        soil_dryness (int | None): The rate at which the berry tree dries out the soil as it grows. Higher values
            indicate faster drying.
        firmness (NamedAPIResource): A reference to the firmness category of the berry.
        flavors (list[BerryFlavorMap]): The flavors associated with the berry and their respective potencies.
        item (NamedAPIResource): A reference to the item associated with the berry.
        natural_gift_type (NamedAPIResource): A reference to the type of the move Natural Gift when used with this
            berry.
    """

    id: int
    name: str
    growth_time: int | None
    max_harvest: int | None
    natural_gift_power: int | None
    size: int | None
    smoothness: int | None
    soil_dryness: int | None
    firmness: NamedAPIResource
    flavors: list[BerryFlavorMap]
    item: NamedAPIResource
    natural_gift_type: NamedAPIResource


@dataclass(frozen=True)
class BerryFlavorMap:
    """Represent a flavor and its potency for a berry.

    Attributes:
        potency (int): The potency of the referenced flavor for this berry.
        flavor (NamedAPIResource): A reference to the berry flavor.
    """

    potency: int
    flavor: NamedAPIResource
