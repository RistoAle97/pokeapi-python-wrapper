"""Sprites module."""

from pathlib import Path

from pydantic import validate_call
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class Sprite:
    """Represent a sprite retrieved from PokéAPI.

    Attributes:
        url (str): The URL from which the sprite was retrieved.
        content (bytes): The binary content of the sprite image.
    """

    url: str
    content: bytes

    @validate_call
    def save(self, path: str | Path) -> None:
        """Save the sprite image to the specified path.

        Args:
            path (str | Path): The destination path where the sprite will be saved.
        """
        with open(path, "wb") as img:
            img.write(self.content)
