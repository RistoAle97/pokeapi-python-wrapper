"""Contest Effects endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Effect, FlavorText


@dataclass(frozen=True)
class ContestEffect:
    """Represent a contest effect resource returned by PokéAPI.

    Contest effects describe how moves influence appeal and affect opponents during Pokémon Contests.

    This model corresponds to the `/api/v2/contest-effect/{id}/` endpoint.

    Attributes:
        id (int): The unique identifier of the contest effect.
        appeal (int): The base number of hearts awarded to the user of a move with this effect.
        jam (int): The base number of hearts the user's opponent loses when this effect is used.
        effect_entries (list[Effect]): The descriptions of this contest effect in different languages.
        flavor_text_entries (list[FlavorText]): The flavor text descriptions of this contest effect in different
            languages.
    """

    id: int
    appeal: int
    jam: int
    effect_entries: list[Effect]
    flavor_text_entries: list[FlavorText]
