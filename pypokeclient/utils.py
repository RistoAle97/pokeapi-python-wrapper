"""Sprites module."""

import re
from pathlib import Path
from typing import Any

from pydantic import validate_call
from pydantic.dataclasses import dataclass

from ._api import __all__

ENDPOINTS = {
    re.sub(r"(\w)([A-Z])", r"\1-\2", endpoint).lower()
    for endpoint in __all__
    if endpoint not in {"APIResourceList", "LocationAreaEncounter", "NamedAPIResourceList"}
}
UNNAMED_ENDPOINTS = {"characteristic", "contest-effect", "evolution-chain", "machine", "super-contest-effect"}
NAMED_ENDPOINTS = ENDPOINTS - UNNAMED_ENDPOINTS


@dataclass(frozen=True)
class Sprite:
    """A dataclass representing a sprite."""

    url: str
    content: bytes | Any

    @validate_call
    def save(self, path: str | Path) -> None:
        """Save the sprite at the specified path.

        Args:
            path (str | Path): the path where the sprint will be saved.
        """
        with open(path, "wb") as img:
            img.write(self.content)
