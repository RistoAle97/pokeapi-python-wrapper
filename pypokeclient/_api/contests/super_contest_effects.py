"""Super Contest Effects endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import FlavorText, NamedAPIResource


@dataclass(frozen=True)
class SuperContestEffect:
    id: int
    appeal: int
    flavor_text_entries: list[FlavorText]
    moves: list[NamedAPIResource]
