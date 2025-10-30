## :material-hammer-wrench: Simple usage
The asynchronous client is represented by the `AsyncClient` class which uses aiohttp under the hood for performing every request to PokéAPI. Using the client is straightforward and simple
```python
import asyncio

from pypokeclient import AsyncClient


async def fetch_data():
    async_client = AsyncClient()
    pokemon = await async_client.get_pokemon("fuecoco")
    return pokemon


pokemon = asyncio.run(fetch_data())
```
Alternatively, you can use the client via context manager and requests session will be closed automatically once the context is exited
```python
import asyncio

from pypokeclient import AsyncClient


async def fetch_data():
    async with AsyncClient() as async_client:
        pokemon = await async_client.get_pokemon("fuecoco")

    return pokemon


pokemon = asyncio.run(fetch_data())
```
Behind the scenes, the client uses an `httpx.AsyncClient` object to perform the requests, as such you can define your own custom HTTP client
```python
import httpx
from pypokeclient import AsyncClient

# Let's say I want to use HTTP/2
http_client = httpx.AsyncClient(http2=True)
with AsyncClient(http_client) as async_client:
    pokemon = await async_client.get_pokemon("fuecoco")
```

---

## :material-content-save: Caching
Caching is done by leveraging the [hishel](https://hishel.com/dev/) package, as such it is highly advised to take a look its documentation.

```python
import logging

from hishel import AsyncSqliteStorage
from hishel.httpx import AsyncCacheClient
from pypokeclient import AsyncClient


async def fetch_data():
    http_client = AsyncCacheClient(
        storage=AsyncSqliteStorage(database_path="pypokeclient_cache.db")
    )
    async with AsyncClient(http_client) as async_client:
        # Not in the cache, the response will be saved inside of it
        pokemon = await async_client.get_pokemon("fuecoco")

        # This time the response is taken from the cache if not expired
        pokemon = await async_client.get_pokemon("fuecoco")

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
INFO - The asynchronous client is ready and using the cache at '.cache\hishel\pypokeclient_cache.db'.
INFO - [200] Request to https://pokeapi.co/api/v2/pokemon/fuecoco.
INFO - [200] Cached request to https://pokeapi.co/api/v2/pokemon/fuecoco.
INFO - Closed session for the asynchronous client.
```
