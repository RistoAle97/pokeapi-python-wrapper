"""Base client for interacting with PokéAPI."""

import logging
import re
from abc import ABC, abstractmethod
from typing import Any

from pydantic import validate_call

from . import _api

logger = logging.getLogger(__name__.split(".")[0])

# Define the set of named and unnamed endpoints
ENDPOINTS = {
    re.sub(r"(\w)([A-Z])", r"\1-\2", endpoint).lower()
    for endpoint in _api.__all__
    if endpoint not in ["APIResourceList", "LocationAreaEncounter", "NamedAPIResourceList"]
}
_UNNAMED_ENDPOINTS = {"characteristic", "contest-effect", "evolution-chain", "machine", "super-contest-effect"}
_NAMED_ENDPOINTS = ENDPOINTS - _UNNAMED_ENDPOINTS


class BaseClient(ABC):
    """Base class for both the synchronous and asynchronous clients.

    This class enables the interaction with all the PokeAPI endpoints and allows to cache the responses locally.
    """

    def __init__(
        self,
        api_url: str = "https://pokeapi.co/api/v2/",
    ) -> None:
        """Initializes a Client object.

        Args:
            api_url (str): the API base url. Defaults to "https://pokeapi.co/api/v2/".
        """
        self.api_url = api_url

    @abstractmethod
    def _api_request(self, url: str) -> Any:
        pass

    @abstractmethod
    def _get_resource[T](self, endpoint: str, key: int | str, model: type[T]) -> T:
        """Function to fetch an API resource and parse it into a Pydantic dataclass.

        Args:
            endpoint (str): the endpoint (e.g. "pokemon", "berry", "item").
            key (int | str): id or name of the resource.
            model (type[T]): model class to parse the response.

        Returns:
            T: parsed response as the given Pydantic dataclass.
        """
        pass

    @validate_call
    def get_resource_list(
        self, endpoint: str, limit: int = 20, offset: int = 0
    ) -> _api.NamedAPIResourceList | _api.APIResourceList | None:
        """Get a list of resource data.

        Args:
            endpoint (str): the endpoint (e.g. "pokemon", "berry", "item").
            limit (int, optional): limits the number of elements to fetch. Defaults to 20.
            offset (int, optional): offset needed to move to next page. Defaults to 0.

        Returns:
            NamedAPIResourceList | APIResourceList | None: the parsed response from the API if the passed endpoint is
                among the list of available endpoints.
        """
        if endpoint in _UNNAMED_ENDPOINTS:
            model = _api.APIResourceList
        elif endpoint in _NAMED_ENDPOINTS:
            model = _api.NamedAPIResourceList
        else:
            logger.error(f"{endpoint} is not among the list of available endpoints.")
            return None

        return self._get_resource(endpoint, f"?limit={limit}&offset={offset}", model)

    # Berries group
    @validate_call
    def get_berry(self, key: int | str) -> _api.Berry:
        """Get data about a berry.

        Args:
            key (int | str): id or name of the berry.

        Returns:
            Berry: the parsed response from the API.
        """
        return self._get_resource("berry", key, _api.Berry)

    @validate_call
    def get_berry_firmness(self, key: int | str) -> _api.BerryFirmness:
        """Get data about a berry firmness.

        Args:
            key (int | str): id or name of the berry firmness.

        Returns:
            BerryFirmness: the parsed response from the API.
        """
        return self._get_resource("berry-firmness", key, _api.BerryFirmness)

    @validate_call
    def get_berry_flavor(self, key: int | str) -> _api.BerryFlavor:
        """Get data about a berry flavor.

        Args:
            key (int | str): id or name of the berry flavor.

        Returns:
            BerryFlavor: the parsed response from the API.
        """
        return self._get_resource("berry-flavor", key, _api.BerryFlavor)

    # Contests group
    @validate_call
    def get_contest_type(self, key: int | str) -> _api.ContestType:
        """Get data about a contest type.

        Args:
            key (int | str): id or name of the contest type.

        Returns:
            ContestType: the parsed response from the API.
        """
        return self._get_resource("contest-type", key, _api.ContestType)

    @validate_call
    def get_contest_effect(self, key: int) -> _api.ContestEffect:
        """Get data about a contest effect.

        Args:
            key (int): id of the contest effect.

        Returns:
            ContestEffect: the parsed response from the API.
        """
        return self._get_resource("contest-effect", key, _api.ContestEffect)

    @validate_call
    def get_super_contest_effect(self, key: int) -> _api.SuperContestEffect:
        """Get data about a super contest effect.

        Args:
            key (int): id of the super contest effect.

        Returns:
            SuperContestEffect: the parsed response from the API.
        """
        return self._get_resource("super-contest-effect", key, _api.SuperContestEffect)

    # Encounters group
    @validate_call
    def get_encounter_method(self, key: int | str) -> _api.EncounterMethod:
        """Get data about an encounter method.

        Args:
            key (int | str): id or name of the encounter method.

        Returns:
            EncounterMethod: the parsed response from the API.
        """
        return self._get_resource("encounter-method", key, _api.EncounterMethod)

    @validate_call
    def get_encounter_condition(self, key: int | str) -> _api.EncounterCondition:
        """Get data about an encounter condition.

        Args:
            key (int | str): id or name of the encounter condition.

        Returns:
            EncounterCondition: the parsed response from the API.
        """
        return self._get_resource("encounter-condition", key, _api.EncounterCondition)

    @validate_call
    def get_encounter_condition_value(self, key: int | str) -> _api.EncounterConditionValue:
        """Get data about an encounter condition value.

        Args:
            key (int | str): id or name of the encounter condition.

        Returns:
            EncounterConditionValue: the parsed response from the API.
        """
        return self._get_resource("encounter-condition-value", key, _api.EncounterConditionValue)

    # Evolution group
    @validate_call
    def get_evolution_chain(self, key: int) -> _api.EvolutionChain:
        """Get data about an evolution chain.

        Args:
            key (int): id of the evolution chain.

        Returns:
            EvolutionChain: the parsed response from the API.
        """
        return self._get_resource("evolution-chain", key, _api.EvolutionChain)

    @validate_call
    def get_evolution_trigger(self, key: int | str) -> _api.EvolutionTrigger:
        """Get data about an evolution trigger.

        Args:
            key (int | str): id or name of the evolution trigger.

        Returns:
            EvolutionTrigger: the parsed response from the API.
        """
        return self._get_resource("evolution-trigger", key, _api.EvolutionTrigger)

    # Games group
    @validate_call
    def get_generation(self, key: int | str) -> _api.Generation:
        """Get data about a generation.

        Args:
            key (int | str): id or name of the generation.

        Returns:
            Generation: the parsed response from the API.
        """
        return self._get_resource("generation", key, _api.Generation)

    @validate_call
    def get_pokedex(self, key: int | str) -> _api.Pokedex:
        """Get data about a Pokédex.

        Args:
            key (int | str): id or name of the Pokédex.

        Returns:
            Pokedex: the parsed response from the API.
        """
        return self._get_resource("pokedex", key, _api.Pokedex)

    @validate_call
    def get_version_group(self, key: int | str) -> _api.VersionGroup:
        """Get data about a version group.

        Args:
            key (int | str): id or name of the version group.

        Returns:
            VersionGroup: the parsed response from the API.
        """
        return self._get_resource("version-group", key, _api.VersionGroup)

    @validate_call
    def get_version(self, key: int | str) -> _api.Version:
        """Get data about a version.

        Args:
            key (int | str): id or name of the version.

        Returns:
            Version: the parsed response from the API.
        """
        return self._get_resource("version", key, _api.Version)

    # Items group
    @validate_call
    def get_item(self, key: int | str) -> _api.Item:
        """Get data about an item.

        Args:
            key (int | str): id or name of the item.

        Returns:
            Item: the parsed response from the API.
        """
        return self._get_resource("item", key, _api.Item)

    @validate_call
    def get_item_attribute(self, key: int | str) -> _api.ItemAttribute:
        """Get data about an item attribute.

        Args:
            key (int | str): id or name of the item attribute.

        Returns:
            ItemAttribute: the parsed response from the API.
        """
        return self._get_resource("item-attribute", key, _api.ItemAttribute)

    @validate_call
    def get_item_category(self, key: int | str) -> _api.ItemCategory:
        """Get data about an item category.

        Args:
            key (int | str): id or name of the item category.

        Returns:
            ItemCategory: the parsed response from the API.
        """
        return self._get_resource("item-category", key, _api.ItemCategory)

    @validate_call
    def get_item_fling_effect(self, key: int | str) -> _api.ItemFlingEffect:
        """Get data about an item fling effect.

        Args:
            key (int | str): id or name of the item fling effect.

        Returns:
            ItemFlingEffect: the parsed response from the API.
        """
        return self._get_resource("item-fling-effect", key, _api.ItemFlingEffect)

    @validate_call
    def get_item_pocket(self, key: int | str) -> _api.ItemPocket:
        """Get data about an item pocket.

        Args:
            key (int | str): id or name of the item pocket.

        Returns:
            ItemPocket: the parsed response from the API.
        """
        return self._get_resource("item-pocket", key, _api.ItemPocket)

    # Locations group
    @validate_call
    def get_location(self, key: int | str) -> _api.Location:
        """Get data about a location.

        Args:
            key (int | str): id or name of the location.

        Returns:
            Location: the parsed response from the API.
        """
        return self._get_resource("location", key, _api.Location)

    @validate_call
    def get_location_area(self, key: int | str) -> _api.LocationArea:
        """Get data about a location area.

        Args:
            key (int | str): id or name of the location area.

        Returns:
            LocationArea: the parsed response from the API.
        """
        return self._get_resource("location-area", key, _api.LocationArea)

    @validate_call
    def get_pal_park_area(self, key: int | str) -> _api.PalParkArea:
        """Get data about a Pal Park area.

        Args:
            key (int | str): id or name of the Pal Park area.

        Returns:
            PalParkArea: the parsed response from the API.
        """
        return self._get_resource("pal-park-area", key, _api.PalParkArea)

    @validate_call
    def get_regions(self, key: int | str) -> _api.Region:
        """Get data about a region.

        Args:
            key (int | str): id or name of the region.

        Returns:
            Region: the parsed response from the API.
        """
        return self._get_resource("region", key, _api.Region)

    # Machines group
    @validate_call
    def get_machine(self, key: int) -> _api.Machine:
        """Get data about a machine.

        Args:
            key (int): id of the machine.

        Returns:
            Machine: the parsed response from the API.
        """
        return self._get_resource("machine", key, _api.Machine)

    # Moves group
    @validate_call
    def get_move(self, key: int | str) -> _api.Move:
        """Get data about a move.

        Args:
            key (int | str): id or name of the move.

        Returns:
            Move: the parsed response from the API.
        """
        return self._get_resource("move", key, _api.Move)

    @validate_call
    def get_move_ailment(self, key: int | str) -> _api.MoveAilment:
        """Get data about a move ailment.

        Args:
            key (int | str): id or name of the move ailment.

        Returns:
            MoveAilment: the parsed response from the API.
        """
        return self._get_resource("move-ailment", key, _api.MoveAilment)

    @validate_call
    def get_move_battle_style(self, key: int | str) -> _api.MoveBattleStyle:
        """Get data about a move battle style.

        Args:
            key (int | str): id or name of the move battle style.

        Returns:
            MoveBattleStyle: the parsed response from the API.
        """
        return self._get_resource("move-battle-style", key, _api.MoveBattleStyle)

    @validate_call
    def get_move_category(self, key: int | str) -> _api.MoveCategory:
        """Get data about a move category.

        Args:
            key (int | str): id or name of the move category.

        Returns:
            MoveCategory: the parsed response from the API.
        """
        return self._get_resource("move-category", key, _api.MoveCategory)

    @validate_call
    def get_damage_class(self, key: int | str) -> _api.MoveDamageClass:
        """Get data about a move damage class.

        Args:
            key (int | str): id or name of the move damage class.

        Returns:
            MoveDamageClass: the parsed response from the API.
        """
        return self._get_resource("move-damage-class", key, _api.MoveDamageClass)

    @validate_call
    def get_move_learn_method(self, key: int | str) -> _api.MoveLearnMethod:
        """Get data about a move learn method.

        Args:
            key (int | str): id or name of the move learn method.

        Returns:
            MoveLearnMethod: the parsed response from the API.
        """
        return self._get_resource("move-learn-method", key, _api.MoveLearnMethod)

    @validate_call
    def get_move_target(self, key: int | str) -> _api.MoveTarget:
        """Get data about a move target.

        Args:
            key (int | str): id or name of the move target.

        Returns:
            MoveTarget: the parsed response from the API.
        """
        return self._get_resource("move-target", key, _api.MoveTarget)

    # Pokémon group
    @validate_call
    def get_ability(self, key: int | str) -> _api.Ability:
        """Get data about an ability.

        Args:
            key (int | str): id or name of the ability.

        Returns:
            Ability: the parsed response from the API.
        """
        return self._get_resource("ability", key, _api.Ability)

    @validate_call
    def get_characteristic(self, key: int) -> _api.Characteristic:
        """Get data about a characteristic.

        Args:
            key (int): id of the characteristic.

        Returns:
            Characteristic: the parsed response from the API.
        """
        return self._get_resource("characteristic", key, _api.Characteristic)

    @validate_call
    def get_egg_group(self, key: int | str) -> _api.EggGroup:
        """Get data about an egg group.

        Args:
            key (int | str): id or name of the egg group.

        Returns:
            EggGroup: the parsed response from the API.
        """
        return self._get_resource("egg-group", key, _api.EggGroup)

    @validate_call
    def get_gender(self, key: int | str) -> _api.Gender:
        """Get data about a gender.

        Args:
            key (int | str): id or name of the gender.

        Returns:
            Gender: the parsed response from the API.
        """
        return self._get_resource("gender", key, _api.Gender)

    @validate_call
    def get_growth_rate(self, key: int | str) -> _api.GrowthRate:
        """Get data about a growth rate.

        Args:
            key (int | str): id or name of the growth rate.

        Returns:
            GrowthRate: the parsed response from the API.
        """
        return self._get_resource("growth-rate", key, _api.GrowthRate)

    @validate_call
    def get_nature(self, key: int | str) -> _api.Nature:
        """Get data about a nature.

        Args:
            key (int | str): id or name of the nature.

        Returns:
            Nature: the parsed response from the API.
        """
        return self._get_resource("nature", key, _api.Nature)

    @validate_call
    def get_pokeathlon_stat(self, key: int | str) -> _api.PokeathlonStat:
        """Get data about a Pokéathlon stat.

        Args:
            key (int | str): id or name of the Pokéathlon stat.

        Returns:
            PokeathlonStat: the parsed response from the API.
        """
        return self._get_resource("pokeathlon-stat", key, _api.PokeathlonStat)

    @validate_call
    def get_pokemon(self, key: int | str) -> _api.Pokemon:
        """Get infos about a pokémon.

        Args:
            key (int | str): id or name of the pokémon

        Returns:
            Pokemon: the parsed response from the API.
        """
        return self._get_resource("pokemon", key, _api.Pokemon)

    @validate_call
    def get_pokemon_location_area(self, key: int | str) -> list[_api.LocationAreaEncounter]:
        """Get data about a Pokémon's encounters in a location area.

        Args:
            key (int | str): id or name of the Pokémon.

        Returns:
            LocationAreaEncounter: the parsed response from the API.
        """
        response = self._api_request(f"{self.api_url}pokemon/{key}/encounters")
        return [_api.LocationAreaEncounter(**encounter) for encounter in response.json()]

    @validate_call
    def get_pokemon_color(self, key: int | str) -> _api.PokemonColor:
        """Get data about a Pokémon color.

        Args:
            key (int | str): id or name of the Pokémon color.

        Returns:
            PokemonColor: the parsed response from the API.
        """
        return self._get_resource("pokemon-color", key, _api.PokemonColor)

    @validate_call
    def get_pokemon_form(self, key: int | str) -> _api.PokemonForm:
        """Get data about a Pokémon form.

        Args:
            key (int | str): id or name of the Pokémon form.

        Returns:
            PokemonForm: the parsed response from the API.
        """
        return self._get_resource("pokemon-form", key, _api.PokemonForm)

    @validate_call
    def get_pokemon_habitat(self, key: int | str) -> _api.PokemonHabitat:
        """Get data about a Pokémon habitat.

        Args:
            key (int | str): id or name of the Pokémon habitat.

        Returns:
            PokemonHabitat: the parsed response from the API.
        """
        return self._get_resource("pokemon-habitat", key, _api.PokemonHabitat)

    @validate_call
    def get_pokemon_shape(self, key: int | str) -> _api.PokemonShape:
        """Get data about a Pokémon shape.

        Args:
            key (int | str): id or name of the Pokémon shape.

        Returns:
            PokemonShape: the parsed response from the API.
        """
        return self._get_resource("pokemon-shape", key, _api.PokemonShape)

    @validate_call
    def get_pokemon_species(self, key: int | str) -> _api.PokemonSpecies:
        """Get data about a Pokémon species.

        Args:
            key (int | str): id or name of the Pokémon species.

        Returns:
            PokemonSpecies: the parsed response from the API.
        """
        return self._get_resource("pokemon-species", key, _api.PokemonSpecies)

    @validate_call
    def get_stat(self, key: int | str) -> _api.Stat:
        """Get data about a stat.

        Args:
            key (int | str): id or name of the stat.

        Returns:
            Stat: the parsed response from the API.
        """
        return self._get_resource("stat", key, _api.Stat)

    @validate_call
    def get_type(self, key: int | str) -> _api.Type:
        """Get data about a type.

        Args:
            key (int | str): id or name of the type.

        Returns:
            Type: the parsed response from the API.
        """
        return self._get_resource("type", key, _api.Type)

    # Utility group
    @validate_call
    def get_language(self, key: int | str) -> _api.Language:
        """Get infos about a language.

        Args:
            key (int | str): id or name of the pokémon

        Returns:
            Language: the parsed response from the API.
        """
        return self._get_resource("language", key, _api.Language)
