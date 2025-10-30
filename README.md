<div align="center">

# PyPokéClient

<img src="https://raw.githubusercontent.com/RistoAle97/pokeapi-python-wrapper/main/docs/logo.png" width=25% />

**Synchronous and asynchronous clients to fetch data from PokéAPI.**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/python/cpython)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://github.com/pydantic/pydantic)

[![PyPI](https://img.shields.io/pypi/v/pypokeclient.svg?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/pypokeclient/)
[![Python versions](https://img.shields.io/pypi/pyversions/pypokeclient.svg?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/pypokeclient/)

</div>

---

## 📌 Features

- **Coverage:** all PokéAPI endpoints are covered.
- **Data validation:** uses Pydantic dataclasses for the API implementation.
- **Flexibility:** can choose between synchronous and asynchronous clients.
- **Caching:** can employ a local cache system for faster responses and to respect PokéAPI Fair Use policy.

Please have a look at the [documentation](https://ristoale97.github.io/pokeapi-python-wrapper/) for more details about the package.

---

## 📦 Installation

```bash
# It is highly recommended to use uv
uv pip install pypokeclient

# But you can also install the package via pip
pip install pypokeclient
```

---

## 🛠️ How to use

You can choose whether to use the synchronous client
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

## 💾 Caching the results

>[!IMPORTANT]
>Please refer to the [hishel](https://hishel.com/dev/) documentation for more details about the caching system.
```python
import logging

from hishel import SyncSqliteStorage
from hishel.httpx import SyncCacheClient
from pypokeclient import Client

# Set up the logger
logger = logging.getLogger("pypokeclient")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(name)s - %(levelname)s - %(message)s"))
logger.addHandler(console_handler)

# Set up the underlying HTTP client
http_client = SyncCacheClient(
    storage=SyncSqliteStorage(database_path="pypokeclient_cache.db")
)

# Fetch data
with Client(http_client) as sync_client:
    pokemon = sync_client.get_pokemon("fuecoco")
    pokemon = sync_client.get_pokemon("fuecoco")

    # The sprites are cached too
    sprite = sync_client.get_sprite(pokemon.sprites.front_default)
    sprite = sync_client.get_sprite(pokemon.sprites.front_default)

    # You can also save the sprites locally if needed
    sprite.save("fuecoco.png")
```
The output will be the following
```
pypokeclient - INFO - The synchronous client is ready and using the cache at .cache\hishel\pypokeclient_cache.db'.
pypokeclient - INFO - [200] Request to https://pokeapi.co/api/v2/pokemon/fuecoco.
pypokeclient - INFO - [200] Cached request to https://pokeapi.co/api/v2/pokemon/fuecoco.
pypokeclient - INFO - [200] Request to https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/909.png.
pypokeclient - INFO - [200] Cached request to https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/909.png.
pypokeclient - INFO - Closed session for the synchronous client.
```

---

## 📝 License

This project is [MIT licensed](https://github.com/RistoAle97/pokeapi-python-wrapper/blob/main/LICENSE).
