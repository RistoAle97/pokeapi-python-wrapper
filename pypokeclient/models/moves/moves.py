"""Moves endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import APIResource, MachineVersionDetail, Name, NamedAPIResource, VerboseEffect
from pypokeclient.models.pokemon.abilities import AbilityEffectChange


@dataclass(frozen=True)
class Move:
    """Represent a move resource returned by PokéAPI.

    Moves are actions that Pokémon can use in battle and, in some cases, outside battle. They have properties that
    determine their accuracy, power, effects, targets, and availability across game versions.

    This model corresponds to the `/api/v2/move/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the move.
        name (str): The name of the move.
        accuracy (int | None): The probability of the move hitting its target, expressed as a percentage, or `None` if
            no value is specified.
        effect_chance (int | None): The probability of an additional move effect occurring, expressed as a percentage,
            or `None` if no value is specified.
        pp (int): The base number of times the move can be used before its PP must be restored.
        priority (int): The priority used to determine the move's execution order relative to other moves.
        power (int | None): The base power of the move, or `None` if no base power is specified.
        contest_combos (_ContestComboSets | None): The combinations of moves that can be used before or after this move
            in Contests and Super Contests, or `None` if no combinations are defined.
        contest_type (NamedAPIResource | None): The Contest category associated with this move, or `None` if none is
            defined.
        contest_effect (APIResource | None): The effect of this move in Contests, or `None` if no effect is defined.
        damage_class (NamedAPIResource): The damage class of the move, such as physical, special, or status.
        effect_entries (list[VerboseEffect]): The localized descriptions of the move's effects.
        effect_changes (list[AbilityEffectChange]): The changes to the move's effects across different version groups.
        learned_by_pokemon (list[NamedAPIResource]): The Pokémon that can learn this move.
        flavor_text_entries (list[_MoveFlavorText]): The flavor text descriptions of this move across different game
            versions.
        generation (NamedAPIResource): The generation in which the move was introduced.
        machines (list[MachineVersionDetail]): The machines that teach this move in different version groups.
        meta (_MoveMetaData | None): Additional metadata describing the move's effects and battle mechanics, or `None`
            if unavailable.
        names (list[Name]): The localized names of this move in different languages.
        past_values (list[_PastMoveStatValues]): The historical values of the move's properties across different version
            groups.
        stat_changes (list[_MoveStatChange]): The stat changes caused by the move.
        super_contest_effect (APIResource | None): The effect of this move in Super Contests, or `None` if no effect is
            defined.
        target (NamedAPIResource): The type of target affected by this move.
        type (NamedAPIResource): The elemental type of the move.
    """

    id: int
    name: str
    accuracy: int | None
    effect_chance: int | None
    pp: int
    priority: int
    power: int | None
    contest_combos: _ContestComboSets | None
    contest_type: NamedAPIResource | None
    contest_effect: APIResource | None
    damage_class: NamedAPIResource
    effect_entries: list[VerboseEffect]
    effect_changes: list[AbilityEffectChange]
    learned_by_pokemon: list[NamedAPIResource]
    flavor_text_entries: list[_MoveFlavorText]
    generation: NamedAPIResource
    machines: list[MachineVersionDetail]
    meta: _MoveMetaData | None
    names: list[Name]
    past_values: list[_PastMoveStatValues]
    stat_changes: list[_MoveStatChange]
    super_contest_effect: APIResource | None
    target: NamedAPIResource
    type: NamedAPIResource


@dataclass(frozen=True)
class _ContestComboSets:
    """Represent the contest combinations associated with a move.

    Attributes:
        normal (_ContestComboDetail | None): The combinations available in regular Contests, or `None` if no
            combinations are defined.
        super (_ContestComboDetail | None): The combinations available in Super Contests, or `None` if no combinations
            are defined.
    """

    normal: _ContestComboDetail | None
    super: _ContestComboDetail | None


@dataclass(frozen=True)
class _ContestComboDetail:
    """Represent the moves that can be combined with another move in a contest.

    Attributes:
        use_before (list[NamedAPIResource] | None): The moves that can be used before this move, or `None` if no such
            moves are defined.
        use_after (list[NamedAPIResource] | None): The moves that can be used after this move, or `None` if no such
            moves are defined.
    """

    use_before: list[NamedAPIResource] | None
    use_after: list[NamedAPIResource] | None


@dataclass(frozen=True)
class _MoveFlavorText:
    """Represent a localized flavor text entry for a move.

    Attributes:
        flavor_text (str): The flavor text describing the move.
        language (NamedAPIResource): The language in which the text is written.
        version_group (NamedAPIResource): The version group associated with this flavor text.
    """

    flavor_text: str
    language: NamedAPIResource
    version_group: NamedAPIResource


@dataclass(frozen=True)
class _MoveMetaData:
    """Represent additional battle metadata for a move.

    Attributes:
        ailment (NamedAPIResource): The status ailment inflicted by the move.
        category (NamedAPIResource): The category describing the move's general effect, such as damage or an ailment.
        min_hits (int | None): The minimum number of hits made by the move, or `None` if it always hits only once.
        max_hits (int | None): The maximum number of hits made by the move, or `None` if it always hits only once.
        min_turns (int | None): The minimum number of turns the move's effect lasts, or `None` if it lasts only one
            turn.
        max_turns (int | None): The maximum number of turns the move's effect lasts, or `None` if it lasts only one
            turn.
        drain (int): The percentage of damage dealt that is recovered as HP, or the percentage applied as recoil damage
            when negative.
        healing (int): The percentage of the user's maximum HP restored.
        crit_rate (int): The critical hit rate bonus associated with the move.
        ailment_chance (int): The probability of inflicting the ailment, expressed as a percentage.
        flinch_chance (int): The probability of causing the target to flinch, expressed as a percentage.
        stat_chance (int): The probability of triggering a stat change, expressed as a percentage.
    """

    ailment: NamedAPIResource
    category: NamedAPIResource
    min_hits: int | None
    max_hits: int | None
    min_turns: int | None
    max_turns: int | None
    drain: int
    healing: int
    crit_rate: int
    ailment_chance: int
    flinch_chance: int
    stat_chance: int


@dataclass(frozen=True)
class _MoveStatChange:
    """Represent a stat change caused by a move.

    Attributes:
        change (int): The number of stages by which the stat changes. Positive values indicate an increase, while
            negative values indicate a decrease.
        stat (NamedAPIResource): The stat affected by the move.
    """

    change: int
    stat: NamedAPIResource


@dataclass(frozen=True)
class _PastMoveStatValues:
    """Represent historical move properties for a particular version group.

    Attributes:
        accuracy (int | None): The move's accuracy during the specified version group, or `None` if no value is
            specified.
        effect_chance (int | None): The probability of the move's additional effect occurring, expressed as a
            percentage, or `None` if no value is specified.
        power (int | None): The move's base power during the specified version group, or `None` if no value is
            specified.
        pp (int | None): The move's base PP during the specified version group, or `None` if no value is specified.
        effect_entries (list[VerboseEffect]): The localized descriptions of the move's effects during the specified
            version group.
        type (NamedAPIResource | None): The move's elemental type during the specified version group, or `None` if no
            type is specified.
        version_group (NamedAPIResource): The version group to which these historical values apply.
    """

    accuracy: int | None
    effect_chance: int | None
    power: int | None
    pp: int | None
    effect_entries: list[VerboseEffect]
    type: NamedAPIResource | None
    version_group: NamedAPIResource
