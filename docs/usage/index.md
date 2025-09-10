This documentation briefly explains how to work with both the synchronous and asynchronous clients, and describes how the caching mechanism works.

!!! warning "Caching"
    - Please refer to the [requests-cache](https://requests-cache.readthedocs.io/en/stable/index.html) and [aiohttp-client-cache](https://aiohttp-client-cache.readthedocs.io/en/stable/index.html) documentation for more details about the caching system.
    - It is not advised to use the same cache for both versions of the client as the two aforementioned packages work differently.
    - Using the context manager is the preferred way when using a cache as the client will delete the expired responses from the cache on setup and will automatically close the session at the end.
