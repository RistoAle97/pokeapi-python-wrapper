---
tags:
    - Usage
---

If you prefer to build your own API client, including your own caching mechanism, you can still take advantage of Pydantic validation and data models provided by pypokeclient.
```python
import requests
from pypokeclient.models import Pokemon

resp = requests.get("https://pokeapi.co/api/v2/pokemon/fuecoco")
resp.raise_for_status()
pokemon = Pokemon(**resp.json())
```
