"""Version endpoint."""

from pydantic.dataclasses import dataclass

from ..common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class Version:
    id: int
    name: str
    names: list[Name]
    version_group: NamedAPIResource
