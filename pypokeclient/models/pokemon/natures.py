"""Natures endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import Name, NamedAPIResource


@dataclass(frozen=True)
class Nature:
    """Represent a nature resource returned by PokéAPI.

    Natures influence Pokémon stat growth and determine their preferences for certain flavors. They also affect move
    selection in the Battle Palace and Battle Tent.

    This model corresponds to the `/api/v2/nature/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the nature.
        name (str): The name of the nature.
        decreased_stat (NamedAPIResource | None): The stat decreased by 10% for Pokémon with this nature, or `None` if
            no stat is decreased.
        increased_stat (NamedAPIResource | None): The stat increased by 10% for Pokémon with this nature, or `None` if
            no stat is increased.
        hates_flavor (NamedAPIResource | None): The berry flavor disliked by Pokémon with this nature, or `None` if no
            flavor is specified.
        likes_flavor (NamedAPIResource | None): The berry flavor preferred by Pokémon with this nature, or `None` if no
            flavor is specified.
        pokeathlon_stat_changes (list[NatureStatChange]): The changes this nature applies to Pokéathlon stats.
        move_battle_style_preferences (list[MoveBattleStylePreference]): The move battle styles preferred by Pokémon
            with this nature, depending on their remaining HP.
        names (list[Name]): The localized names of this nature in different languages.
    """

    id: int
    name: str
    decreased_stat: NamedAPIResource | None
    increased_stat: NamedAPIResource | None
    hates_flavor: NamedAPIResource | None
    likes_flavor: NamedAPIResource | None
    pokeathlon_stat_changes: list[NatureStatChange]
    move_battle_style_preferences: list[MoveBattleStylePreference]
    names: list[Name]


@dataclass(frozen=True)
class NatureStatChange:
    """Represent the effect of a nature on a Pokéathlon stat.

    Attributes:
        max_change (int): The amount by which this nature changes the associated Pokéathlon stat.
        pokeathlon_stat (NamedAPIResource): The Pokéathlon stat affected by this nature.
    """

    max_change: int
    pokeathlon_stat: NamedAPIResource


@dataclass(frozen=True)
class MoveBattleStylePreference:
    """Represent a Pokémon nature's preference for a move battle style.

    Attributes:
        low_hp_preference (int): The chance, expressed as a percentage, of choosing this battle style when the
            Pokémon's HP is below half.
        high_hp_preference (int): The chance, expressed as a percentage, of choosing this battle style when the
            Pokémon's HP is above half.
        move_battle_style (NamedAPIResource): The move battle style associated with these preferences.
    """

    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: NamedAPIResource
