<div align="center">

# PyPokéClient
<img src="https://github.com/RistoAle97/pokeapi-python-wrapper/blob/main/assets/logo.png" width=300/>

**Synchronous and asynchronous clients to fetch data from PokéAPI.**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/python/cpython)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://github.com/pydantic/pydantic)

</div>

---

## :notebook: Documentation
>[!WARNING]
>The documentation is still work in progress.

**Main features:**
- Covers all the PokéAPI endpoints.
- Uses Pydantic for data validation.
- Can choose between synchronous and asynchronous clients.
- Can employ a local cache system for faster responses and to respect PokéAPI Fair Use policy.

---

## :package: Installation
>[!IMPORTANT]
>- This package requires python >= 3.12.
>- The package will published on PyPI as soon as it is ready.

```bash
# It is highly recommended to use uv
uv pip install git+https://github.com/RistoAle97/pokeapi-python-wrapper

# But you can also install the package simply with pip
pip install git+https://github.com/RistoAle97/pokeapi-python-wrapper
```

---

## :hammer_and_wrench: How to use
You can choose whether to use a synchronous client
```python
from pypokeclient import Client

# Simple usage
client = Client()
pokemon = client.get_pokemon("fuecoco")

# Or with context manager
with Client() as client:
  pokemon = client.get_pokemon("fuecoco")
```
or the asynchronous one
```python
import asyncio

from pypokeclient import AsyncClient


async def fetch_data():
  # Simple usage
  client = AsyncClient()
  pokemon = await client.get_pokemon("fuecoco")

  # With context manager
  async with AsyncClient() as client:
    pokemon = await client.get_pokemon("fuecoco")

asyncio.run(fetch_data())
```

---

## :floppy_disk: Caching the results
>[!IMPORTANT]
>- Please refer to the [requests-cache](https://requests-cache.readthedocs.io/en/stable/index.html) and [aiohttp-client-cache](https://aiohttp-client-cache.readthedocs.io/en/stable/index.html) documentations for more details about the caching system.
>- It is not advised to use the same cache for both versions of the client as the two aforementioned packages work differently.
>- Using the context manager is the preferred way when using a cache as the client will delete the expired responses from the cache on setup and will automatically close the session at the end.
```python
import logging

from requests_cache import CachedSession
from pypokeclient import Client


# Set up the logger
logger = logging.getLogger("pypokeclient")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(name)s - %(levelname)s - %(message)s"))
logger.addHandler(console_handler)

# Fetch data
with Client(cached_session=CachedSession("pypokeclient-sync")) as sync_client:
    pokemon = sync_client.get_pokemon("fuecoco")
    pokemon = sync_client.get_pokemon("fuecoco")
```
The output will be the following
```
pypokeclient - INFO - Synchronous client is up and ready using CachedSession.
pypokeclient - INFO - [200] Request to https://pokeapi.co/api/v2/pokemon/fuecoco.
pypokeclient - INFO - [200] Cached request to https://pokeapi.co/api/v2/pokemon/fuecoco.
pypokeclient - INFO - Closed session for synchronous client.
```
