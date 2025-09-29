"""Item Fling Effects endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Effect, NamedAPIResource


@dataclass(frozen=True)
class ItemFlingEffect:
    id: int
    name: str
    effect_entries: list[Effect]
    items: list[NamedAPIResource]
