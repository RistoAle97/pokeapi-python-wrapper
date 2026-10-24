"""Evolution Chains endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import NamedAPIResource


@dataclass(frozen=True)
class EvolutionChain:
    """Represent an evolution chain resource returned by PokéAPI.

    Evolution chains describe the evolutionary family tree of a Pokémon species, including the possible evolutions and
    the conditions required for each evolutionary transition.

    This model corresponds to the `/api/v2/evolution-chain/{id}/` endpoint.

    Attributes:
        id (int): The unique identifier of the evolution chain.
        baby_trigger_item (NamedAPIResource | None): The item associated with hatching a baby Pokémon instead of its
            non-baby form.
        chain (_ChainLink): The base link of the evolution chain, containing the first species and all subsequent
            evolutionary branches.
    """

    id: int
    baby_trigger_item: NamedAPIResource | None
    chain: _ChainLink


@dataclass(frozen=True)
class _ChainLink:
    """Represent a link in an evolution chain.

    Each link describes a Pokémon species and its position in the evolution chain, including the conditions associated
    with its evolution and any subsequent evolutions.

    Attributes:
        is_baby (bool): Whether this link represents a baby Pokémon.
        species (NamedAPIResource): The Pokémon species represented by this link.
        evolution_details (list[_EvolutionDetail]): The conditions associated with this species' evolution from the
            preceding stage.
        evolves_to (list[_ChainLink]): The links representing the species this Pokémon can evolve into.
    """

    is_baby: bool
    species: NamedAPIResource
    evolution_details: list[_EvolutionDetail]
    evolves_to: list[_ChainLink]


@dataclass(frozen=True)
class _EvolutionDetail:
    """Represent the conditions required for an evolution.

    This model describes the requirements and circumstances under which a Pokémon species evolves into another species
    or form.

    Attributes:
        version_group (NamedAPIResource | None): The game version group associated with this evolution.
        is_default (bool): Whether this is the default evolution for the Pokémon variety in the main series games.
        item (NamedAPIResource | None): The item required to trigger the evolution.
        trigger (NamedAPIResource): The event that triggers the evolution.
        gender (int | None): The gender ID required for the evolving Pokémon.
        held_item (NamedAPIResource | None): The item the evolving Pokémon must hold when the evolution is triggered.
        known_move (NamedAPIResource | None): The move the evolving Pokémon must know when the evolution is triggered.
        known_move_type (NamedAPIResource | None): The move type the evolving Pokémon must know when the evolution is
            triggered.
        location (NamedAPIResource | None): The location where the evolution must be triggered.
        min_level (int | None): The minimum level required for the evolution.
        min_happiness (int | None): The minimum happiness value required for the evolution.
        min_beauty (int | None): The minimum Beauty value required for the evolution.
        min_affection (int | None): The minimum affection value required for the evolution.
        near_special_rock (bool): Whether the evolution requires proximity to a Moss Rock or Icy Rock.
        needs_multiplayer (bool): Whether the evolution requires multiplayer play.
        needs_overworld_rain (bool): Whether rain in the overworld is required for the evolution.
        party_species (NamedAPIResource | None): The Pokémon species that must be in the player's party during the
            evolution.
        party_type (NamedAPIResource | None): The type a Pokémon in the player's party must have during the evolution.
        relative_physical_stats (int | None): The required relationship between Attack and Defense: -1 means Attack
            is lower, 0 means they are equal, and 1 means Attack is higher.
        time_of_day (str): The required time of day for the evolution, such as `day`, `night`, `dusk`, or `full-moon`.
        trade_species (NamedAPIResource | None): The Pokémon species for which the evolving Pokémon must be traded.
        turn_upside_down (bool): Whether the Nintendo 3DS must be turned upside down while the Pokémon levels up.
        region (NamedAPIResource | None): The region in which the evolution must occur.
        required_pokemon_form (NamedAPIResource | None): The Pokémon form required for the evolution.
        evolved_pokemon_form (NamedAPIResource | None): The Pokémon form resulting from the evolution.
        used_move (NamedAPIResource | None): The move that must be used during the evolution trigger event.
        min_move_count (int | None): The minimum number of times the required move must be used for the evolution.
        min_steps (int | None): The minimum number of steps required for the evolution.
        min_damage_taken (int | None): The minimum amount of damage that must be taken during the evolution trigger
            event.
        allowed_natures (list[NamedAPIResource] | None): The natures permitted for the evolving Pokémon.
        condition_expression (_EvolutionConditionExpression | None): An expression describing additional
            variable-dependent evolution requirements.
    """

    version_group: NamedAPIResource | None
    is_default: bool
    item: NamedAPIResource | None
    trigger: NamedAPIResource
    gender: int | None
    held_item: NamedAPIResource | None
    known_move: NamedAPIResource | None
    known_move_type: NamedAPIResource | None
    location: NamedAPIResource | None
    min_level: int | None
    min_happiness: int | None
    min_beauty: int | None
    min_affection: int | None
    near_special_rock: bool
    needs_multiplayer: bool
    needs_overworld_rain: bool
    party_species: NamedAPIResource | None
    party_type: NamedAPIResource | None
    relative_physical_stats: int | None
    time_of_day: str
    trade_species: NamedAPIResource | None
    turn_upside_down: bool
    region: NamedAPIResource | None
    required_pokemon_form: NamedAPIResource | None
    evolved_pokemon_form: NamedAPIResource | None
    used_move: NamedAPIResource | None
    min_move_count: int | None
    min_steps: int | None
    min_damage_taken: int | None
    allowed_natures: list[NamedAPIResource] | None
    condition_expression: _EvolutionConditionExpression | None


@dataclass(frozen=True)
class _EvolutionConditionExpression:
    """Represent a variable-dependent evolution condition.

    The expression uses Reverse Polish Notation (RPN) to evaluate conditions involving evolution variables, such as a
    Pokémon's encryption constant.

    Attributes:
        expression (str): The RPN expression evaluated to determine whether the evolution condition is satisfied.
        percentage_chance (float | None): The percentage chance of evolution when this condition is satisfied, from 0
            to 100.
        variables (list[NamedAPIResource]): The evolution variables referenced by the expression.
    """

    expression: str
    percentage_chance: float | None
    variables: list[NamedAPIResource]
