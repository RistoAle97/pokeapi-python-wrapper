## :material-hammer-wrench: Simple usage
The asynchronous client is represented by the `AsyncClient` class which uses aiohttp under the hood for performing every request to PokéAPI. Using the client is straightforward and simple
```python
import asyncio

from pypokeclient import AsyncClient


async def fetch_data():
    client = AsyncClient()
    pokemon = await client.get_pokemon("fuecoco")
    return pokemon


pokemon = asyncio.run(fetch_data())
```

Alternatively, you can use the client via context manager and requests session will be closed automatically once the context is exited
```python
import asyncio

from pypokeclient import AsyncClient


async def fetch_data():
    async with AsyncClient() as client:
        pokemon = await client.get_pokemon("fuecoco")

    return pokemon


pokemon = asyncio.run(fetch_data())
```

---

## :material-content-save: Caching
Caching is done by leveraging the [aiohttp-client-cache](https://aiohttp-client-cache.readthedocs.io/en/stable/index.html) package, as such it is highly advised to take a look its documentation. Using the context is manager is preferred as the cache is automatically cleared of the expired responses during the setup.

```python
import logging

from pypokeclient import AsyncClient
from aiohttp_client_cache import CachedSession, SQLiteBackend


async def fetch_data():
    # You can choose between many different backends
    cache_backend = SQLiteBackend("pypokeclient-async")
    session = CachedSession(cache=cache_backend)

    async with AsyncClient(session=session) as client:
        # Not in the cache, the response will be saved inside of it
        pokemon = await client.get_pokemon("fuecoco")

        # This time the response is taken from the cache if not expired
        pokemon = await client.get_pokemon("fuecoco")

    return pokemon


# Set up the logger
logger = logging.getLogger("pypokeclient")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setFormatter(
    logging.Formatter("%(levelname)s - %(message)s")
)
logger.addHandler(console_handler)

# Run the async method
pokemon = asyncio.run(fetch_data())
```

In the logs you can clearly see that the second response was cached
```
INFO - Asynchronous client is up and ready using CachedSession.
INFO - [200] Request to https://pokeapi.co/api/v2/pokemon/fuecoco.
INFO - [200] Cached request to https://pokeapi.co/api/v2/pokemon/fuecoco.
INFO - Closed session for asynchronous client.
```

If needed, you can clear the cache by
```python
# Assuming that you've already created a Client object
client.clear_cache()  # will log an error if no cache is used
```
