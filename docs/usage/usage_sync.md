## :material-hammer-wrench: Simple usage
The synchronous client is represented by the `Client` class which uses requests under the hood for performing every request to PokéAPI. Using the client is straightforward and simple
```python
from pypokeclient import Client

sync_client = Client()
pokemon = sync_client.get_pokemon("fuecoco")
```
Alternatively, you can use the client via context manager and requests session will be closed automatically once the context is exited
```python
from pypokeclient import Client

with Client() as sync_client:
    pokemon = sync_client.get_pokemon("fuecoco")
```
Behind the scenes, the client uses an `httpx.Client` object to perform the requests, as such you can define your own custom HTTP client
```python
import httpx
from pypokeclient import Client

# Let's say I want to use HTTP/2
http_client = httpx.Client(http2=True)
with Client(http_client) as sync_client:
    pokemon = sync_client.get_pokemon("fuecoco")
```

---

## :material-content-save: Caching
Caching is done by leveraging the [hishel](https://hishel.com/dev/) package, as such it is highly advised to take a look its documentation.

```python
import logging

from hishel import SyncSqliteStorage
from hishel.httpx import SyncCacheClient
from pypokeclient import Client

# Set up the logger
logger = logging.getLogger("pypokeclient")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setFormatter(
    logging.Formatter("%(levelname)s - %(message)s")
)
logger.addHandler(console_handler)

# Note that hishel.SyncCacheClient is a subclass of httpx.Client
http_client = SyncCacheClient(
    storage=SyncSqliteStorage(database_path="pypokeclient_cache.db")
)
with Client(http_client) as sync_client:
    # Not in the cache, the response will be saved inside of it
    pokemon = sync_client.get_pokemon("fuecoco")

    # This time the response is taken from the cache if not expired
    pokemon = sync_client.get_pokemon("fuecoco")
```

In the logs you can clearly see that the second response was cached
```
INFO - The synchronous client is ready and using the cache at '.cache\hishel\pypokeclient_cache.db'.
INFO - [200] Request to https://pokeapi.co/api/v2/pokemon/fuecoco.
INFO - [200] Cached request to https://pokeapi.co/api/v2/pokemon/fuecoco.
INFO - Closed session for the synchronous client.
```
