## :material-hammer-wrench: Simple usage
The synchronous client is represented by the `Client` class which uses requests under the hood for performing every request to PokéAPI. Using the client is straightforward and simple
```python
from pypokeclient import Client

client = Client()
pokemon = client.get_pokemon("fuecoco")
```
Alternatively, you can use the client via context manager and requests session will be closed automatically once the context is exited
```python
from pypokeclient import Client

with Client() as sync_client:
    pokemon = client.get_pokemon("fuecoco")
```

---

## :material-content-save: Caching
Caching is done by leveraging the [requests-cache](https://requests-cache.readthedocs.io/en/stable/index.html) package, as such it is highly advised to take a look its documentation. Using the context is manager is preferred as the cache is automatically cleared of the expired responses during the setup.

```python
import logging

from pypokeclient import Client
from requests_cache import CachedSession

# Set up the logger
logger = logging.getLogger("pypokeclient")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setFormatter(
    logging.Formatter("%(levelname)s - %(message)s")
)
logger.addHandler(console_handler)

# By default, a .sqlite db will be created
with Client(session=CachedSession("pypokeclient-sync")) as client:
    # Not in the cache, the response will be saved inside of it
    pokemon = client.get_pokemon("fuecoco")

    # This time the response is taken from the cache if not expired
    pokemon = client.get_pokemon("fuecoco")
```

In the logs you can clearly see that the second response was cached
```
INFO - Synchronous client is up and ready using CachedSession.
INFO - [200] Request to https://pokeapi.co/api/v2/pokemon/fuecoco.
INFO - [200] Cached request to https://pokeapi.co/api/v2/pokemon/fuecoco.
INFO - Closed session for synchronous client.
```

If needed, you can clear the cache by
```python
# Assuming that you've already created a Client object
client.clear_cache()  # will log an error if no cache is used
```
