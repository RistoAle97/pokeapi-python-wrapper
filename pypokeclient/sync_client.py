"""Synchronous client for interacting with PokéAPI."""

import logging
from types import TracebackType

import httpx2
from pydantic import validate_call

from . import models

logger = logging.getLogger(__name__.split(".")[0])


class Client:
    """Synchronous version of the client."""

    def __init__(self, http_client: httpx2.Client | None = None) -> None:
        """Initializes a `Client` object.

        Args:
            http_client (httpx2.Client): an `httpx2.Client` used to send request to the API. Please note that
                `hishel.SyncCacheClient` is a subclass of `httpx2.Client` so you can pass an instance of that class
                if you want to cache the responses.
        """
        self._owns_http_client = False
        if http_client is None:
            self._http_client = httpx2.Client(base_url="https://pokeapi.co/api/v2/")
            self._owns_http_client = True
        else:
            self._http_client = http_client

        logger.debug("Synchronous client initialized.")

    # ===========================================
    # Context manager methods
    # ===========================================
    def __enter__(self) -> "Client":
        """Returns this client for use as a context manager.

        Returns:
            Client: an instance of the synchronous client.
        """
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_val: BaseException | None = None,
        exc_tb: TracebackType | None = None,
    ) -> None:
        """Closes the session.

        Args:
            exc_type (type[BaseException] | None): exception type. Defaults to None.
            exc_val (BaseException | None): exception value. Defaults to None.
            exc_tb (TracebackType | None): exception traceback. Defaults to None.
        """
        del exc_type, exc_val, exc_tb
        if self._owns_http_client:
            self._http_client.close()
            logger.debug("Closed internally owned HTTP client.")
        else:
            logger.debug("Released wrapper, caller-owned HTTP client remains open.")

    # ===========================================
    # HTTP request methods
    # ===========================================
    def _api_request(self, url: str) -> httpx2.Response:
        """Sends an API request.

        Args:
            url (str): the url to which the request will be sent.

        Returns:
            httpx2.Response: the non-parsed response from the API.
        """
        response = self._http_client.get(url)
        response.raise_for_status()
        is_cached = response.extensions.get("hishel_from_cache", False)
        request_type = "Cached request" if is_cached else "Request"
        logger.debug("[%s] %s to %s", response.status_code, request_type, response.url)
        return response

    def _get_resource[T](self, endpoint: str, key: int | str, model: type[T]) -> T:
        response = self._api_request(f"{endpoint}/{key}")
        return model(**response.json())

    def _get_resources[T](self, endpoint: str, key: int | str, model: type[T]) -> list[T]:
        response = self._api_request(f"{endpoint}/{key}")
        return [model(**unparsed_data) for unparsed_data in response.json()]

    # ===========================================
    # Resource lists
    # ===========================================
    @validate_call
    def get_resource_list(
        self, endpoint: str, limit: int = 20, offset: int = 0
    ) -> models.NamedAPIResourceList | models.APIResourceList:
        """Get a list of resource data.

        Args:
            endpoint (str): the endpoint (e.g. "pokemon", "berry", "item").
            limit (int): limits the number of elements to fetch. Defaults to 20.
            offset (int): offset needed to move to next page. Defaults to 0.

        Returns:
            NamedAPIResourceList | APIResourceList: the parsed response from the API if the passed endpoint is
                among the list of available endpoints.
        """
        if limit < 0:
            raise ValueError("limit must be non-negative")

        if offset < 0:
            raise ValueError("offset must be non-negative")

        if endpoint in models.UNNAMED_ENDPOINTS:
            return self._get_resource(endpoint, f"?limit={limit}&offset={offset}", models.APIResourceList)
        elif endpoint in models.NAMED_ENDPOINTS:
            return self._get_resource(endpoint, f"?limit={limit}&offset={offset}", models.NamedAPIResourceList)
        else:
            raise ValueError(
                f"Unknown endpoint: {endpoint!r}.\nSupported endpoints: {', '.join(sorted(models.ENDPOINTS))}"
            )

    # ===========================================
    # Berries group
    # ===========================================
    @validate_call
    def get_berry(self, key: int | str) -> models.Berry:
        """Get data about a berry.

        Args:
            key (int | str): id or name of the berry.

        Returns:
            Berry: the parsed response from the API.
        """
        return self._get_resource("berry", key, models.Berry)

    @validate_call
    def get_berry_firmness(self, key: int | str) -> models.BerryFirmness:
        """Get data about a berry firmness.

        Args:
            key (int | str): id or name of the berry firmness.

        Returns:
            BerryFirmness: the parsed response from the API.
        """
        return self._get_resource("berry-firmness", key, models.BerryFirmness)

    @validate_call
    def get_berry_flavor(self, key: int | str) -> models.BerryFlavor:
        """Get data about a berry flavor.

        Args:
            key (int | str): id or name of the berry flavor.

        Returns:
            BerryFlavor: the parsed response from the API.
        """
        return self._get_resource("berry-flavor", key, models.BerryFlavor)

    # ===========================================
    # Contests group
    # ===========================================
    @validate_call
    def get_contest_type(self, key: int | str) -> models.ContestType:
        """Get data about a contest type.

        Args:
            key (int | str): id or name of the contest type.

        Returns:
            ContestType: the parsed response from the API.
        """
        return self._get_resource("contest-type", key, models.ContestType)

    @validate_call
    def get_contest_effect(self, key: int) -> models.ContestEffect:
        """Get data about a contest effect.

        Args:
            key (int): id of the contest effect.

        Returns:
            ContestEffect: the parsed response from the API.
        """
        return self._get_resource("contest-effect", key, models.ContestEffect)

    @validate_call
    def get_super_contest_effect(self, key: int) -> models.SuperContestEffect:
        """Get data about a super contest effect.

        Args:
            key (int): id of the super contest effect.

        Returns:
            SuperContestEffect: the parsed response from the API.
        """
        return self._get_resource("super-contest-effect", key, models.SuperContestEffect)

    # ===========================================
    # Currencies group
    # ===========================================
    @validate_call
    def get_currency(self, key: int | str) -> models.Currency:
        """Get data about a currency.

        Args:
            key (int | str): id or name of the currency.

        Returns:
            Currency: the parsed response from the API.
        """
        return self._get_resource("currency", key, models.Currency)

    # ===========================================
    # Encounters group
    # ===========================================
    @validate_call
    def get_encounter_method(self, key: int | str) -> models.EncounterMethod:
        """Get data about an encounter method.

        Args:
            key (int | str): id or name of the encounter method.

        Returns:
            EncounterMethod: the parsed response from the API.
        """
        return self._get_resource("encounter-method", key, models.EncounterMethod)

    @validate_call
    def get_encounter_condition(self, key: int | str) -> models.EncounterCondition:
        """Get data about an encounter condition.

        Args:
            key (int | str): id or name of the encounter condition.

        Returns:
            EncounterCondition: the parsed response from the API.
        """
        return self._get_resource("encounter-condition", key, models.EncounterCondition)

    @validate_call
    def get_encounter_condition_value(self, key: int | str) -> models.EncounterConditionValue:
        """Get data about an encounter condition value.

        Args:
            key (int | str): id or name of the encounter condition.

        Returns:
            EncounterConditionValue: the parsed response from the API.
        """
        return self._get_resource("encounter-condition-value", key, models.EncounterConditionValue)

    # ===========================================
    # Evolution group
    # ===========================================
    @validate_call
    def get_evolution_chain(self, key: int) -> models.EvolutionChain:
        """Get data about an evolution chain.

        Args:
            key (int): id of the evolution chain.

        Returns:
            EvolutionChain: the parsed response from the API.
        """
        return self._get_resource("evolution-chain", key, models.EvolutionChain)

    @validate_call
    def get_evolution_trigger(self, key: int | str) -> models.EvolutionTrigger:
        """Get data about an evolution trigger.

        Args:
            key (int | str): id or name of the evolution trigger.

        Returns:
            EvolutionTrigger: the parsed response from the API.
        """
        return self._get_resource("evolution-trigger", key, models.EvolutionTrigger)

    @validate_call
    def get_evolution_variable(self, key: int | str) -> models.EvolutionVariable:
        """Get data about an evolution variable.

        Args:
            key (int | str): id or name of the evolution variable.

        Returns:
            EvolutionVariable: the parsed response from the API.
        """
        return self._get_resource("evolution-variable", key, models.EvolutionVariable)

    # ===========================================
    # Games group
    # ===========================================
    @validate_call
    def get_generation(self, key: int | str) -> models.Generation:
        """Get data about a generation.

        Args:
            key (int | str): id or name of the generation.

        Returns:
            Generation: the parsed response from the API.
        """
        return self._get_resource("generation", key, models.Generation)

    @validate_call
    def get_pokedex(self, key: int | str) -> models.Pokedex:
        """Get data about a Pokédex.

        Args:
            key (int | str): id or name of the Pokédex.

        Returns:
            Pokedex: the parsed response from the API.
        """
        return self._get_resource("pokedex", key, models.Pokedex)

    @validate_call
    def get_version_group(self, key: int | str) -> models.VersionGroup:
        """Get data about a version group.

        Args:
            key (int | str): id or name of the version group.

        Returns:
            VersionGroup: the parsed response from the API.
        """
        return self._get_resource("version-group", key, models.VersionGroup)

    @validate_call
    def get_version(self, key: int | str) -> models.Version:
        """Get data about a version.

        Args:
            key (int | str): id or name of the version.

        Returns:
            Version: the parsed response from the API.
        """
        return self._get_resource("version", key, models.Version)

    # ===========================================
    # Items group
    # ===========================================
    @validate_call
    def get_item(self, key: int | str) -> models.Item:
        """Get data about an item.

        Args:
            key (int | str): id or name of the item.

        Returns:
            Item: the parsed response from the API.
        """
        return self._get_resource("item", key, models.Item)

    @validate_call
    def get_item_attribute(self, key: int | str) -> models.ItemAttribute:
        """Get data about an item attribute.

        Args:
            key (int | str): id or name of the item attribute.

        Returns:
            ItemAttribute: the parsed response from the API.
        """
        return self._get_resource("item-attribute", key, models.ItemAttribute)

    @validate_call
    def get_item_category(self, key: int | str) -> models.ItemCategory:
        """Get data about an item category.

        Args:
            key (int | str): id or name of the item category.

        Returns:
            ItemCategory: the parsed response from the API.
        """
        return self._get_resource("item-category", key, models.ItemCategory)

    @validate_call
    def get_item_fling_effect(self, key: int | str) -> models.ItemFlingEffect:
        """Get data about an item fling effect.

        Args:
            key (int | str): id or name of the item fling effect.

        Returns:
            ItemFlingEffect: the parsed response from the API.
        """
        return self._get_resource("item-fling-effect", key, models.ItemFlingEffect)

    @validate_call
    def get_item_pocket(self, key: int | str) -> models.ItemPocket:
        """Get data about an item pocket.

        Args:
            key (int | str): id or name of the item pocket.

        Returns:
            ItemPocket: the parsed response from the API.
        """
        return self._get_resource("item-pocket", key, models.ItemPocket)

    # ===========================================
    # Locations group
    # ===========================================
    @validate_call
    def get_location(self, key: int | str) -> models.Location:
        """Get data about a location.

        Args:
            key (int | str): id or name of the location.

        Returns:
            Location: the parsed response from the API.
        """
        return self._get_resource("location", key, models.Location)

    @validate_call
    def get_location_area(self, key: int | str) -> models.LocationArea:
        """Get data about a location area.

        Args:
            key (int | str): id or name of the location area.

        Returns:
            LocationArea: the parsed response from the API.
        """
        return self._get_resource("location-area", key, models.LocationArea)

    @validate_call
    def get_pal_park_area(self, key: int | str) -> models.PalParkArea:
        """Get data about a Pal Park area.

        Args:
            key (int | str): id or name of the Pal Park area.

        Returns:
            PalParkArea: the parsed response from the API.
        """
        return self._get_resource("pal-park-area", key, models.PalParkArea)

    @validate_call
    def get_region(self, key: int | str) -> models.Region:
        """Get data about a region.

        Args:
            key (int | str): id or name of the region.

        Returns:
            Region: the parsed response from the API.
        """
        return self._get_resource("region", key, models.Region)

    # ===========================================
    # Machines group
    # ===========================================
    @validate_call
    def get_machine(self, key: int) -> models.Machine:
        """Get data about a machine.

        Args:
            key (int): id of the machine.

        Returns:
            Machine: the parsed response from the API.
        """
        return self._get_resource("machine", key, models.Machine)

    # ===========================================
    # Moves group
    # ===========================================
    @validate_call
    def get_move(self, key: int | str) -> models.Move:
        """Get data about a move.

        Args:
            key (int | str): id or name of the move.

        Returns:
            Move: the parsed response from the API.
        """
        return self._get_resource("move", key, models.Move)

    @validate_call
    def get_move_ailment(self, key: int | str) -> models.MoveAilment:
        """Get data about a move ailment.

        Args:
            key (int | str): id or name of the move ailment.

        Returns:
            MoveAilment: the parsed response from the API.
        """
        return self._get_resource("move-ailment", key, models.MoveAilment)

    @validate_call
    def get_move_battle_style(self, key: int | str) -> models.MoveBattleStyle:
        """Get data about a move battle style.

        Args:
            key (int | str): id or name of the move battle style.

        Returns:
            MoveBattleStyle: the parsed response from the API.
        """
        return self._get_resource("move-battle-style", key, models.MoveBattleStyle)

    @validate_call
    def get_move_category(self, key: int | str) -> models.MoveCategory:
        """Get data about a move category.

        Args:
            key (int | str): id or name of the move category.

        Returns:
            MoveCategory: the parsed response from the API.
        """
        return self._get_resource("move-category", key, models.MoveCategory)

    @validate_call
    def get_damage_class(self, key: int | str) -> models.MoveDamageClass:
        """Get data about a move damage class.

        Args:
            key (int | str): id or name of the move damage class.

        Returns:
            MoveDamageClass: the parsed response from the API.
        """
        return self._get_resource("move-damage-class", key, models.MoveDamageClass)

    @validate_call
    def get_move_learn_method(self, key: int | str) -> models.MoveLearnMethod:
        """Get data about a move learn method.

        Args:
            key (int | str): id or name of the move learn method.

        Returns:
            MoveLearnMethod: the parsed response from the API.
        """
        return self._get_resource("move-learn-method", key, models.MoveLearnMethod)

    @validate_call
    def get_move_target(self, key: int | str) -> models.MoveTarget:
        """Get data about a move target.

        Args:
            key (int | str): id or name of the move target.

        Returns:
            MoveTarget: the parsed response from the API.
        """
        return self._get_resource("move-target", key, models.MoveTarget)

    # ===========================================
    # Pokémon group
    # ===========================================
    @validate_call
    def get_ability(self, key: int | str) -> models.Ability:
        """Get data about an ability.

        Args:
            key (int | str): id or name of the ability.

        Returns:
            Ability: the parsed response from the API.
        """
        return self._get_resource("ability", key, models.Ability)

    @validate_call
    def get_characteristic(self, key: int) -> models.Characteristic:
        """Get data about a characteristic.

        Args:
            key (int): id of the characteristic.

        Returns:
            Characteristic: the parsed response from the API.
        """
        return self._get_resource("characteristic", key, models.Characteristic)

    @validate_call
    def get_egg_group(self, key: int | str) -> models.EggGroup:
        """Get data about an egg group.

        Args:
            key (int | str): id or name of the egg group.

        Returns:
            EggGroup: the parsed response from the API.
        """
        return self._get_resource("egg-group", key, models.EggGroup)

    @validate_call
    def get_gender(self, key: int | str) -> models.Gender:
        """Get data about a gender.

        Args:
            key (int | str): id or name of the gender.

        Returns:
            Gender: the parsed response from the API.
        """
        return self._get_resource("gender", key, models.Gender)

    @validate_call
    def get_growth_rate(self, key: int | str) -> models.GrowthRate:
        """Get data about a growth rate.

        Args:
            key (int | str): id or name of the growth rate.

        Returns:
            GrowthRate: the parsed response from the API.
        """
        return self._get_resource("growth-rate", key, models.GrowthRate)

    @validate_call
    def get_nature(self, key: int | str) -> models.Nature:
        """Get data about a nature.

        Args:
            key (int | str): id or name of the nature.

        Returns:
            Nature: the parsed response from the API.
        """
        return self._get_resource("nature", key, models.Nature)

    @validate_call
    def get_pokeathlon_stat(self, key: int | str) -> models.PokeathlonStat:
        """Get data about a Pokéathlon stat.

        Args:
            key (int | str): id or name of the Pokéathlon stat.

        Returns:
            PokeathlonStat: the parsed response from the API.
        """
        return self._get_resource("pokeathlon-stat", key, models.PokeathlonStat)

    @validate_call
    def get_pokemon(self, key: int | str) -> models.Pokemon:
        """Get data about a pokémon.

        Args:
            key (int | str): id or name of the pokémon

        Returns:
            Pokemon: the parsed response from the API.
        """
        return self._get_resource("pokemon", key, models.Pokemon)

    @validate_call
    def get_pokemon_location_area_encounters(self, key: int | str) -> list[models.LocationAreaEncounter]:
        """Get data about a Pokémon's encounters in a location area.

        Args:
            key (int | str): id or name of the Pokémon.

        Returns:
            list[LocationAreaEncounter]: the parsed response from the API.
        """
        return self._get_resources(f"pokemon/{key}/encounters", "", models.LocationAreaEncounter)

    @validate_call
    def get_pokemon_color(self, key: int | str) -> models.PokemonColor:
        """Get data about a Pokémon color.

        Args:
            key (int | str): id or name of the Pokémon color.

        Returns:
            PokemonColor: the parsed response from the API.
        """
        return self._get_resource("pokemon-color", key, models.PokemonColor)

    @validate_call
    def get_pokemon_form(self, key: int | str) -> models.PokemonForm:
        """Get data about a Pokémon form.

        Args:
            key (int | str): id or name of the Pokémon form.

        Returns:
            PokemonForm: the parsed response from the API.
        """
        return self._get_resource("pokemon-form", key, models.PokemonForm)

    @validate_call
    def get_pokemon_habitat(self, key: int | str) -> models.PokemonHabitat:
        """Get data about a Pokémon habitat.

        Args:
            key (int | str): id or name of the Pokémon habitat.

        Returns:
            PokemonHabitat: the parsed response from the API.
        """
        return self._get_resource("pokemon-habitat", key, models.PokemonHabitat)

    @validate_call
    def get_pokemon_shape(self, key: int | str) -> models.PokemonShape:
        """Get data about a Pokémon shape.

        Args:
            key (int | str): id or name of the Pokémon shape.

        Returns:
            PokemonShape: the parsed response from the API.
        """
        return self._get_resource("pokemon-shape", key, models.PokemonShape)

    @validate_call
    def get_pokemon_species(self, key: int | str) -> models.PokemonSpecies:
        """Get data about a Pokémon species.

        Args:
            key (int | str): id or name of the Pokémon species.

        Returns:
            PokemonSpecies: the parsed response from the API.
        """
        return self._get_resource("pokemon-species", key, models.PokemonSpecies)

    @validate_call
    def get_stat(self, key: int | str) -> models.Stat:
        """Get data about a stat.

        Args:
            key (int | str): id or name of the stat.

        Returns:
            Stat: the parsed response from the API.
        """
        return self._get_resource("stat", key, models.Stat)

    @validate_call
    def get_type(self, key: int | str) -> models.Type:
        """Get data about a type.

        Args:
            key (int | str): id or name of the type.

        Returns:
            Type: the parsed response from the API.
        """
        return self._get_resource("type", key, models.Type)

    # ===========================================
    # Utility group
    # ===========================================
    @validate_call
    def get_language(self, key: int | str) -> models.Language:
        """Get info about a language.

        Args:
            key (int | str): id or name of the pokémon

        Returns:
            Language: the parsed response from the API.
        """
        return self._get_resource("language", key, models.Language)

    # ===========================================
    # Sprites
    # ===========================================
    @validate_call
    def get_sprite(self, url: str) -> models.Sprite:
        """Get a sprite from an url.

        Args:
            url (str): the url to the sprite.

        Returns:
            Sprite: a Sprite object useful to save the image.
        """
        response = self._api_request(url)
        return models.Sprite(url, response.content)
