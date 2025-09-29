"""Wrapper for PokéAPI."""
#      ____        ____       _         ____ _ _            _
#     |  _ \ _   _|  _ \ ___ | | _____ / ___| (_) ___ _ __ | |_
#     | |_) | | | | |_) / _ \| |/ / _ \ |   | | |/ _ \ '_ \| __|
#     |  __/| |_| |  __/ (_) |   <  __/ |___| | |  __/ | | | |_
#     |_|    \__, |_|   \___/|_|\_\___|\____|_|_|\___|_| |_|\__|
#            |___/

from .async_client import AsyncClient
from .base_client import ENDPOINTS
from .sync_client import Client

__all__ = ["ENDPOINTS", "AsyncClient", "Client"]
