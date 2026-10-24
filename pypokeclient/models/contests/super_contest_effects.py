"""Super Contest Effects endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import FlavorText, NamedAPIResource


@dataclass(frozen=True)
class SuperContestEffect:
    """Represent a super contest effect resource returned by PokéAPI.

    Super contest effects describe the effects of moves when used in Super Contests.

    This model corresponds to the `https://pokeapi.co/api/v2/super-contest-effect/{id}/` endpoint.

    Attributes:
        id (int): The unique identifier of the super contest effect.
        appeal (int): The level of appeal this super contest effect has.
        flavor_text_entries (list[FlavorText]): The flavor text descriptions of this super contest effect in different
            languages.
        moves (list[NamedAPIResource]): The moves associated with this super contest effect.
    """

    id: int
    appeal: int
    flavor_text_entries: list[FlavorText]
    moves: list[NamedAPIResource]
