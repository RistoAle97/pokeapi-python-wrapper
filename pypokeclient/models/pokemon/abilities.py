"""Abilities endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Effect, Name, NamedAPIResource, VerboseEffect


@dataclass(frozen=True)
class Ability:
    """Represent an ability resource returned by PokéAPI.

    Abilities provide passive effects for Pokémon in battle or in the overworld. Each Pokémon can have one ability at a
    time.

    This model corresponds to the `https://pokeapi.co/api/v2/ability/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the ability.
        name (str): The name of the ability.
        is_main_series (bool): Whether this ability originated in the main series of the Pokémon video games.
        generation (NamedAPIResource): The generation in which this ability was introduced.
        names (list[Name]): The localized names of this ability in different languages.
        effect_entries (list[VerboseEffect]): The descriptions of this ability's effects in different languages.
        effect_changes (list[AbilityEffectChange]): The previous effects this ability had in different version groups.
        flavor_text_entries (list[AbilityFlavorText]): The flavor text descriptions of this ability across different
            game versions.
        pokemon (list[AbilityPokemon]): The Pokémon that can have this ability, including their ability slots and
            hidden ability status.
    """

    id: int
    name: str
    is_main_series: bool
    generation: NamedAPIResource
    names: list[Name]
    effect_entries: list[VerboseEffect]
    effect_changes: list[AbilityEffectChange]
    flavor_text_entries: list[AbilityFlavorText]
    pokemon: list[AbilityPokemon]


@dataclass(frozen=True)
class AbilityEffectChange:
    """Represent a historical change to an ability's effect.

    Attributes:
        effect_entries (list[Effect]): The previous descriptions of the ability's effect in different languages.
        version_group (NamedAPIResource): The version group in which the previous effect applied.
    """

    effect_entries: list[Effect]
    version_group: NamedAPIResource


@dataclass(frozen=True)
class AbilityFlavorText:
    """Represent a localized flavor text entry for an ability.

    Attributes:
        flavor_text (str): The flavor text describing the ability.
        language (NamedAPIResource): The language in which the flavor text is written.
        version_group (NamedAPIResource): The version group associated with this flavor text.
    """

    flavor_text: str
    language: NamedAPIResource
    version_group: NamedAPIResource


@dataclass(frozen=True)
class AbilityPokemon:
    """Represent a Pokémon that can have a particular ability.

    Attributes:
        is_hidden (bool): Whether this ability is a hidden ability for the Pokémon.
        slot (int): The ability slot occupied by this ability for the Pokémon.
        pokemon (NamedAPIResource): The Pokémon that can have this ability.
    """

    is_hidden: bool
    slot: int
    pokemon: NamedAPIResource
