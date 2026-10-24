"""Pokemon Location Areas endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import NamedAPIResource, VersionEncounterDetail


@dataclass(frozen=True)
class LocationAreaEncounter:
    """Represent a location area encounter returned by PokéAPI.

    Location area encounters describe where a Pokémon can be encountered and the conditions under which encounters may
    occur in different game versions.

    This model is returned by the `/api/v2/pokemon/{id or name}/encounters/` endpoint.

    Attributes:
        location_area (NamedAPIResource): The location area where the Pokémon can be encountered.
        version_details (list[VersionEncounterDetail]): The encounter details associated with different game versions.
    """

    location_area: NamedAPIResource
    version_details: list[VersionEncounterDetail]
