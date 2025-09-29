"""Module that represents the api endpoints."""

from .berries import Berry, BerryFirmness, BerryFlavor
from .contests import ContestEffect, ContestType, SuperContestEffect
from .encounters import EncounterCondition, EncounterConditionValue, EncounterMethod
from .evolution import EvolutionChain, EvolutionTrigger
from .games import Generation, Pokedex, Version, VersionGroup
from .items import Item, ItemAttribute, ItemCategory, ItemFlingEffect, ItemPocket
from .languages import Language
from .locations import Location, LocationArea, PalParkArea, Region
from .machines import Machine
from .moves import Move, MoveAilment, MoveBattleStyle, MoveCategory, MoveDamageClass, MoveLearnMethod, MoveTarget
from .pokemon import (
    Ability,
    Characteristic,
    EggGroup,
    Gender,
    GrowthRate,
    LocationAreaEncounter,
    Nature,
    PokeathlonStat,
    Pokemon,
    PokemonColor,
    PokemonForm,
    PokemonHabitat,
    PokemonShape,
    PokemonSpecies,
    Stat,
    Type,
)
from .resource_lists import APIResourceList, NamedAPIResourceList

__all__ = [
    "APIResourceList",
    "Ability",
    "Berry",
    "BerryFirmness",
    "BerryFlavor",
    "Characteristic",
    "ContestEffect",
    "ContestType",
    "EggGroup",
    "EncounterCondition",
    "EncounterConditionValue",
    "EncounterMethod",
    "EvolutionChain",
    "EvolutionTrigger",
    "Gender",
    "Generation",
    "GrowthRate",
    "Item",
    "ItemAttribute",
    "ItemCategory",
    "ItemFlingEffect",
    "ItemPocket",
    "Language",
    "Location",
    "LocationArea",
    "LocationAreaEncounter",
    "Machine",
    "Move",
    "MoveAilment",
    "MoveBattleStyle",
    "MoveCategory",
    "MoveDamageClass",
    "MoveLearnMethod",
    "MoveTarget",
    "NamedAPIResourceList",
    "Nature",
    "PalParkArea",
    "PokeathlonStat",
    "Pokedex",
    "Pokemon",
    "PokemonColor",
    "PokemonForm",
    "PokemonHabitat",
    "PokemonShape",
    "PokemonSpecies",
    "Region",
    "Stat",
    "SuperContestEffect",
    "Type",
    "Version",
    "VersionGroup",
]
