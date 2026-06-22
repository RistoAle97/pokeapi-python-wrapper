import pytest
from unittest.mock import MagicMock

from pypokeclient import Client

ENDPOINTS = [
    ("get_berry", "berry"),
    ("get_berry_firmness", "berry-firmness"),
    ("get_berry_flavor", "berry-flavor"),
    ("get_contest_type", "contest-type"),
    ("get_contest_effect", "contest-effect"),
    ("get_super_contest_effect", "super-contest-effect"),
    ("get_encounter_method", "encounter-method"),
    ("get_encounter_condition", "encounter-condition"),
    ("get_encounter_condition_value", "encounter-condition-value"),
    ("get_evolution_chain", "evolution-chain"),
    ("get_evolution_trigger", "evolution-trigger"),
    ("get_generation", "generation"),
    ("get_pokedex", "pokedex"),
    ("get_version_group", "version-group"),
    ("get_version", "version"),
    ("get_item", "item"),
    ("get_item_attribute", "item-attribute"),
    ("get_item_category", "item-category"),
    ("get_item_fling_effect", "item-fling-effect"),
    ("get_item_pocket", "item-pocket"),
    ("get_location", "location"),
    ("get_location_area", "location-area"),
    ("get_pal_park_area", "pal-park-area"),
    ("get_region", "region"),
    ("get_machine", "machine"),
    ("get_move", "move"),
    ("get_move_ailment", "move-ailment"),
    ("get_move_battle_style", "move-battle-style"),
    ("get_move_category", "move-category"),
    ("get_damage_class", "move-damage-class"),
    ("get_move_learn_method", "move-learn-method"),
    ("get_move_target", "move-target"),
    ("get_ability", "ability"),
    ("get_characteristic", "characteristic"),
    ("get_egg_group", "egg-group"),
    ("get_gender", "gender"),
    ("get_growth_rate", "growth-rate"),
    ("get_nature", "nature"),
    ("get_pokeathlon_stat", "pokeathlon-stat"),
    ("get_pokemon", "pokemon"),
    ("get_pokemon_color", "pokemon-color"),
    ("get_pokemon_form", "pokemon-form"),
    ("get_pokemon_habitat", "pokemon-habitat"),
    ("get_pokemon_shape", "pokemon-shape"),
    ("get_pokemon_species", "pokemon-species"),
    ("get_stat", "stat"),
    ("get_type", "type"),
    ("get_language", "language"),
]

@pytest.mark.parametrize(("method_name", "expected_endpoint"), ENDPOINTS)
def test_resource_endpoint_mapping(method_name: str, expected_endpoint: str):
    client = Client()
    client._get_resource = MagicMock(return_value=None)
    getattr(client, method_name)(1)
    client._get_resource.assert_called_once()
    endpoint = client._get_resource.call_args.args[0]
    assert endpoint == expected_endpoint

def test_pokemon_location_area_endpoint():
    client = Client()
    client._get_resources = MagicMock(return_value=[])
    client.get_pokemon_location_area("fuecoco")
    client._get_resources.assert_called_once()
    endpoint = client._get_resources.call_args.args[0]
    assert endpoint == "pokemon/fuecoco/encounters"
