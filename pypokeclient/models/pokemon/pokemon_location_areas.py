"""Pokemon Location Areas endpoint."""

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import NamedAPIResource, VersionEncounterDetail


@dataclass(frozen=True)
class LocationAreaEncounter:
    location_area: NamedAPIResource
    version_details: list[VersionEncounterDetail]
