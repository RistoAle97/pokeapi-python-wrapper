"""Asynchronous client for interacting with PokéAPI."""

import logging
from types import TracebackType

from aiohttp import ClientResponse, ClientSession
from aiohttp_client_cache import CachedResponse, CachedSession
from requests import HTTPError

from .base_client import BaseClient

logger = logging.getLogger(__name__.split(".")[0])


class AsyncClient(BaseClient):
    """Asynchronous version of the client that leverages the aiohttp package."""

    def __init__(
        self,
        api_url: str = "https://pokeapi.co/api/v2/",
        cached_session: CachedSession | None = None,
    ) -> None:
        """Initializes an AsyncClient object.

        Args:
            api_url (str): the API base url. Defaults to "https://pokeapi.co/api/v2/".
            cached_session (requests_cache.CachedSession | None): the cached session that will store the response
                locally, if None then a requests.Session will be used instead. Defaults to None.
        """
        super().__init__(api_url)
        self._session = cached_session or ClientSession()
        logger.info(f"Asynchronous client is up and ready using {self._session.__class__.__name__}.")

    async def __aenter__(self) -> "AsyncClient":
        """Creates the client and deletes all the expired responses from the cache.

        Returns:
            AsyncClient: an instance of the asynchronous client.
        """
        if isinstance(self._session, CachedSession):
            await self._session.delete_expired_responses()

        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_val: BaseException | None = None,
        exc_tb: TracebackType | None = None,
    ) -> None:
        """Closes the session.

        Args:
            exc_type (type[BaseException] | None): exception type. Defaults to None.
            exc_val (BaseException | None): exception value. Defaults to None.
            exc_tb (TracebackType | None): exception traceback. Defaults to None.
        """
        del exc_type, exc_val, exc_tb
        await self._session.close()
        logger.info("Closed session for asynchronous client.")

    async def _api_request(self, url: str) -> ClientResponse | CachedResponse:
        """Sends an API request.

        Args:
            url (str): the url to which the request will be sent.

        Returns:
            ClientResponse | CachedResponse: the non-parsed response from the API.
        """
        async with self._session.get(url) as response:
            try:
                response.raise_for_status()
            except HTTPError as e:
                raise e

            log_msg = f"[{response.status}] Request to {url}."
            if isinstance(response, CachedResponse):
                log_msg = f"[{response.status}] Cached request to {url}."

            logger.info(log_msg)
            return response

    async def _get_resource[T](self, endpoint: str, key: int | str, model: type[T]) -> T:
        response = await self._api_request(f"{self.api_url}{endpoint}/{key}")
        return model(**await response.json())

    async def clear_cache(self) -> None:
        """Clears the local cache."""
        if isinstance(self._session, CachedSession):
            await self._session.cache.clear()
            logger.info("The cache was cleared.")
        else:
            logger.error("No cache was set up.")
