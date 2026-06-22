from pathlib import Path

from hishel.httpx import SyncCacheClient
from hishel import SyncSqliteStorage
from pypokeclient import Client


def test_cache_hit():
    cached_client = SyncCacheClient(storage=SyncSqliteStorage(database_path=".cache/hishel/test_pypokeclient.db"))
    with Client(cached_client) as client:
        response = client._api_request("https://pokeapi.co/api/v2/pokemon/fuecoco")
        cached_response = client._api_request("https://pokeapi.co/api/v2/pokemon/fuecoco")
        assert not response.extensions.get("hishel_from_cache", False)
        assert cached_response.extensions.get("hishel_from_cache", False)

    Path(".cache/hishel/test_pypokeclient.db").unlink(missing_ok=True)


def test_client_is_not_cached():
    with Client() as client:
        first_response = client._api_request("https://pokeapi.co/api/v2/pokemon/skeledirge")
        second_response = client._api_request("https://pokeapi.co/api/v2/pokemon/skeledirge")
        assert not first_response.extensions.get("hishel_from_cache", False)
        assert not second_response.extensions.get("hishel_from_cache", False)
