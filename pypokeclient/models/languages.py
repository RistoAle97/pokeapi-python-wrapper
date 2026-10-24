"""Languages endpoint."""

from pydantic.dataclasses import dataclass

from .common_models import Name


@dataclass(frozen=True)
class Language:
    """Represent a language resource returned by PokéAPI.

    Languages identify the languages used to translate resource names, descriptions, and other text throughout the API.

    This model corresponds to the `/api/v2/language/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the language.
        name (str): The name of the language, represented by its language code.
        official (bool): Whether the Pokémon games are published in this language.
        iso639 (str): The ISO 639 language code associated with this language.
        iso3166 (str): The ISO 3166 country code associated with this language.
        names (list[Name]): The localized names of this language in different languages.
    """

    id: int
    name: str
    official: bool
    iso639: str
    iso3166: str
    names: list[Name]
