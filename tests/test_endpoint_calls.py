import pytest

from pypokeclient import AsyncClient, Client

ENDPOINT_CASES = [
    # Berries
    ("get_berry", 1),
    ("get_berry_firmness", 1),
    ("get_berry_flavor", 1),

    # Contests
    ("get_contest_type", 1),
    ("get_contest_effect", 1),
    ("get_super_contest_effect", 1),

    # Encounters
    ("get_encounter_method", 1),
    ("get_encounter_condition", 1),
    ("get_encounter_condition_value", 1),

    # Evolution
    ("get_evolution_chain", 1),
    ("get_evolution_trigger", 1),

    # Games
    ("get_generation", 1),
    ("get_pokedex", 1),
    ("get_version_group", 1),
    ("get_version", 1),

    # Items
    ("get_item", 1),
    ("get_item_attribute", 1),
    ("get_item_category", 1),
    ("get_item_fling_effect", 1),
    ("get_item_pocket", 1),

    # Locations
    ("get_location", 1),
    ("get_location_area", 1),
    ("get_pal_park_area", 1),
    ("get_region", 1),

    # Machines
    ("get_machine", 1),

    # Moves
    ("get_move", 1),
    ("get_move_ailment", 1),
    ("get_move_battle_style", 1),
    ("get_move_category", 1),
    ("get_damage_class", 1),
    ("get_move_learn_method", 1),
    ("get_move_target", 1),

    # Pokémon
    ("get_ability", 1),
    ("get_characteristic", 1),
    ("get_egg_group", 1),
    ("get_gender", 1),
    ("get_growth_rate", 1),
    ("get_nature", 1),
    ("get_pokeathlon_stat", 1),
    ("get_pokemon", 1),
    ("get_pokemon_color", 1),
    ("get_pokemon_form", 1),
    ("get_pokemon_habitat", 1),
    ("get_pokemon_shape", 1),
    ("get_pokemon_species", 1),
    ("get_stat", 1),
    ("get_type", 1),

    # Utility
    ("get_language", 1),
]


@pytest.mark.parametrize(("method_name", "key"), ENDPOINT_CASES)
def test_endpoint_returns_data(method_name, key):
    with Client() as client:
        result = getattr(client, method_name)(key)

    assert result is not None
    assert (hasattr(result, "id") or hasattr(result, "name"))


def test_get_pokemon_location_area():
    with Client() as client:
        result = client.get_pokemon_location_area(1)

    assert isinstance(result, list)


@pytest.mark.asyncio
@pytest.mark.parametrize(("method_name", "key"), ENDPOINT_CASES)
async def test_sync_async_same_response(method_name, key):
    with Client() as sync_client:
        sync_result = getattr(sync_client, method_name)(key)

    async with AsyncClient() as async_client:
        async_result = await getattr(async_client, method_name)(key)

    assert sync_result == async_result


@pytest.mark.asyncio
async def test_sync_async_same_pokemon_location_area():
    with Client() as sync_client:
        sync_location_area = sync_client.get_pokemon_location_area(1)

    async with AsyncClient() as async_client:
        async_location_area = await async_client.get_pokemon_location_area(1)

    assert sync_location_area == async_location_area
