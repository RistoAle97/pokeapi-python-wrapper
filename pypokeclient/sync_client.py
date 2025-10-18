"""Synchronous client for interacting with PokéAPI."""

import logging
from types import TracebackType

from requests import HTTPError, Response
from requests.sessions import Session
from requests_cache import CachedResponse, CachedSession, OriginalResponse

from .base_client import BaseClient

logger = logging.getLogger(__name__.split(".")[0])


class Client(BaseClient):
    """Synchronous version of the client that leverages the requests package."""

    def __init__(
        self,
        api_url="https://pokeapi.co/api/v2/",
        cached_session: CachedSession | None = None,
    ) -> None:
        """Initializes a Client object.

        Args:
            api_url (str): the API base url. Defaults to "https://pokeapi.co/api/v2/".
            cached_session (requests_cache.CachedSession | None): the cached session that will store the response
                locally, if None then a requests.Session will be used instead. Defaults to None.
        """
        super().__init__(api_url)
        self._session = cached_session or Session()
        logger.info(f"Synchronous client is up and ready using {self._session.__class__.__name__}.")

    def __enter__(self) -> "Client":
        """Creates the client and deletes all the expired responses from the cache.

        Returns:
            Client: an instance of the synchronous client.
        """
        if isinstance(self._session, CachedSession):
            self._session.cache.delete(expired=True)

        return self

    def __exit__(
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
        self._session.close()
        logger.info("Closed session for synchronous client.")

    def _api_request(self, url: str) -> Response | OriginalResponse | CachedResponse:
        """Sends an API request.

        Args:
            url (str): the url to which the request will be sent.

        Returns:
            Response | OriginalResponse | CachedResponse: the non-parsed response from the API.
        """
        with self._session.get(url) as response:
            try:
                response.raise_for_status()
            except HTTPError as e:
                raise e

            log_msg = f"[{response.status_code}] Request to {url}."
            if isinstance(response, CachedResponse):
                log_msg = f"[{response.status_code}] Cached request to {url}."

            logger.info(log_msg)
            return response

    def _get_resource[T](self, endpoint: str, key: int | str, model: type[T]) -> T:
        response = self._api_request(f"{self.api_url}{endpoint}/{key}")
        return model(**response.json())

    def clear_cache(self) -> None:
        """Clears the local cache."""
        if isinstance(self._session, CachedSession):
            self._session.cache.clear()
            logger.info("The cache was cleared.")
        else:
            logger.error("No cache was set up.")
