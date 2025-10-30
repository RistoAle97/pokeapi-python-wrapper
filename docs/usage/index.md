This documentation briefly explains how to work with both the synchronous and asynchronous clients, and describes how the caching mechanism works.

!!! warning "Caching"
    - Please refer to the [hishel](https://hishel.com/dev/) documentation for more details about the caching system.
    - Using the context manager is the preferred way when using a cache as the client will delete the expired responses from the cache on setup and will automatically close the session at the end.
