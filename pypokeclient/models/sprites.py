"""Sprites module."""

from pathlib import Path
from typing import Any

from pydantic import validate_call
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class Sprite:
    """A dataclass representing a sprite."""

    url: str
    content: bytes | Any

    @validate_call
    def save(self, path: str | Path) -> None:
        """Save the sprite at the specified path.

        Args:
            path (str | Path): the path where the sprite will be saved.
        """
        with open(path, "wb") as img:
            img.write(self.content)
