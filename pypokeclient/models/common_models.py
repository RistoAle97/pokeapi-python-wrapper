"""Base models shared by the endpoints."""

from __future__ import annotations

from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class APIResource:
    """Represent a reference to an API resource returned by PokéAPI.

    Attributes:
        url (str): The URL of the referenced resource.
    """

    url: str


@dataclass(frozen=True)
class Description:
    """Represent a localized description of an API resource.

    Attributes:
        description (str): The description text.
        language (NamedAPIResource): The language in which the description is written.
    """

    description: str
    language: NamedAPIResource


@dataclass(frozen=True)
class Effect:
    """Represent a localized effect description returned by PokéAPI.

    Attributes:
        effect (str): The full effect description.
        language (NamedAPIResource): The language in which the effect description is written.
    """

    effect: str
    language: NamedAPIResource


@dataclass(frozen=True)
class Encounter:
    """Represent the encounter details for a Pokémon.

    Attributes:
        min_level (int): The minimum level of the Pokémon that can be encountered.
        max_level (int): The maximum level of the Pokémon that can be encountered.
        condition_values (list[NamedAPIResource]): The condition values required for this encounter.
        chance (int): The chance of encountering the Pokémon under these conditions, expressed as a percentage.
        method (NamedAPIResource): The method used to encounter the Pokémon.
    """

    min_level: int
    max_level: int
    condition_values: list[NamedAPIResource]
    chance: int
    method: NamedAPIResource


@dataclass(frozen=True)
class FlavorText:
    """Represent flavor text associated with an API resource.

    Attributes:
        flavor_text (str): The flavor text.
        language (NamedAPIResource): The language in which the flavor text is written.
        version (NamedAPIResource | None): The game version associated with the flavor text, or `None` if no version is
            specified.
    """

    flavor_text: str
    language: NamedAPIResource
    version: NamedAPIResource | None = None


@dataclass(frozen=True)
class GenerationGameIndex:
    """Represent a resource's index within a game generation.

    Attributes:
        game_index (int): The index assigned to the resource within the generation.
        generation (NamedAPIResource): The generation to which this index applies.
    """

    game_index: int
    generation: NamedAPIResource


@dataclass(frozen=True)
class MachineVersionDetail:
    """Represent a machine's association with a version group.

    Attributes:
        machine (APIResource): A reference to the machine resource.
        version_group (NamedAPIResource): The version group in which the machine is available.
    """

    machine: APIResource
    version_group: NamedAPIResource


@dataclass(frozen=True)
class Name:
    """Represent a localized name for an API resource.

    Attributes:
        name (str): The localized name.
        language (NamedAPIResource): The language in which the name is written.
    """

    name: str
    language: NamedAPIResource


@dataclass(frozen=True)
class NamedAPIResource:
    """Represent a reference to a named API resource returned by PokéAPI.

    Attributes:
        name (str): The name of the referenced resource.
        url (str): The URL of the referenced resource.
    """

    name: str
    url: str


@dataclass(frozen=True)
class VerboseEffect:
    """Represent a localized effect description with a short summary.

    Attributes:
        effect (str): The full effect description.
        short_effect (str): A concise summary of the effect.
        language (NamedAPIResource): The language in which the descriptions are written.
    """

    effect: str
    short_effect: str
    language: NamedAPIResource


@dataclass(frozen=True)
class VersionEncounterDetail:
    """Represent encounter information for a specific game version.

    Attributes:
        version (NamedAPIResource): The game version to which these details apply.
        max_chance (int): The highest total encounter chance for this version, expressed as a percentage.
        encounter_details (list[Encounter]): The individual encounter details for this version.
    """

    version: NamedAPIResource
    max_chance: int
    encounter_details: list[Encounter]


@dataclass(frozen=True)
class VersionGameIndex:
    """Represent a resource's index within a game version.

    Attributes:
        game_index (int): The index assigned to the resource within the game version.
        version (NamedAPIResource): The game version to which this index applies.
    """

    game_index: int
    version: NamedAPIResource


@dataclass(frozen=True)
class VersionGroupFlavorText:
    """Represent localized flavor text associated with a version group.

    Attributes:
        text (str): The flavor text.
        language (NamedAPIResource): The language in which the text is written.
        version_group (NamedAPIResource): The version group associated with this flavor text.
    """

    text: str
    language: NamedAPIResource
    version_group: NamedAPIResource
