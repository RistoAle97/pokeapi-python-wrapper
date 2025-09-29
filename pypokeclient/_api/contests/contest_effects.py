"""Contest Effects endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import Effect, FlavorText


@dataclass(frozen=True)
class ContestEffect:
    id: int
    appeal: int
    jam: int
    effect_entries: list[Effect]
    flavor_text_entries: list[FlavorText]
