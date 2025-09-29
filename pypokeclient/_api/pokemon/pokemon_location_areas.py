"""Pokemon Location Areas endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient._api.common_models import NamedAPIResource, VersionEncounterDetail


@dataclass(frozen=True)
class LocationAreaEncounter:
    location_area: NamedAPIResource
    version_details: list[VersionEncounterDetail]
