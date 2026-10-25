"""Pokemon Species endpoint."""

from __future__ import annotations

from pydantic.dataclasses import dataclass

from pypokeclient.models.common_models import APIResource, Description, FlavorText, Name, NamedAPIResource


@dataclass(frozen=True)
class PokemonSpecies:
    """Represent a Pokémon species resource returned by PokéAPI.

    Pokémon species define shared characteristics of Pokémon and their varieties, including breeding compatibility,
    evolution, growth, and Pokédex information.

    This model corresponds to the `https://pokeapi.co/api/v2/pokemon-species/{id or name}/` endpoint.

    Attributes:
        id (int): The unique identifier of the Pokémon species.
        name (str): The name of the Pokémon species.
        order (int): The order used to sort species, approximately following National Pokédex order while grouping
            evolutionary families and sorting them by evolutionary stage.
        gender_rate (int): The chance of a Pokémon being female, expressed in eighths, or -1 if the species is
            genderless.
        capture_rate (int): The base capture rate of the species. Higher values indicate that the Pokémon is easier to
            catch.
        base_happiness (int): The base happiness of a Pokémon of this species when caught. Higher values indicate
            greater initial happiness.
        is_baby (bool): Whether this species is classified as a baby Pokémon.
        is_legendary (bool): Whether this species is classified as legendary.
        is_mythical (bool): Whether this species is classified as mythical.
        hatch_counter (int): The initial hatch counter used to determine how many steps are required for an egg of this
            species to hatch.
        has_gender_differences (bool): Whether members of this species have visual differences based on gender.
        forms_switchable (bool): Whether Pokémon of this species can switch between forms.
        growth_rate (NamedAPIResource): The growth rate used to calculate how quickly this species gains experience.
        pokedex_numbers (list[PokemonSpeciesDexEntry]): The Pokédex entries assigned to this species across different
            Pokédexes.
        egg_groups (list[NamedAPIResource]): The egg groups to which this species belongs.
        color (NamedAPIResource): The primary color category associated with this species in the Pokédex.
        shape (NamedAPIResource | None): The physical shape category of this species, or `None` if no shape is
            specified.
        evolves_from_species (NamedAPIResource | None): The species from which this species directly evolves, or `None`
            if it has no preceding evolutionary stage.
        evolution_chain (APIResource): A reference to the evolution chain containing this species.
        habitat (NamedAPIResource | None): The habitat associated with this species, or `None` if no habitat is
            specified.
        generation (NamedAPIResource): The generation in which this species was introduced.
        names (list[Name]): The localized names of this species in different languages.
        pal_park_encounters (list[PalParkEncounterArea]): The Pal Park areas where this species can be encountered,
            including encounter rates and base scores.
        flavor_text_entries (list[FlavorText]): The flavor text descriptions of this species across different game
            versions.
        form_descriptions (list[Description]): The descriptions of the different forms associated with this species.
        genera (list[Genus]): The localized genus classifications of this species in different languages.
        varieties (list[PokemonSpeciesVariety]): The Pokémon varieties associated with this species, including the
            default variety.
    """

    id: int
    name: str
    order: int
    gender_rate: int
    capture_rate: int
    base_happiness: int
    is_baby: bool
    is_legendary: bool
    is_mythical: bool
    hatch_counter: int
    has_gender_differences: bool
    forms_switchable: bool
    growth_rate: NamedAPIResource
    pokedex_numbers: list[PokemonSpeciesDexEntry]
    egg_groups: list[NamedAPIResource]
    color: NamedAPIResource
    shape: NamedAPIResource | None
    evolves_from_species: NamedAPIResource | None
    evolution_chain: APIResource
    habitat: NamedAPIResource | None
    generation: NamedAPIResource
    names: list[Name]
    pal_park_encounters: list[PalParkEncounterArea]
    flavor_text_entries: list[FlavorText]
    form_descriptions: list[Description]
    genera: list[Genus]
    varieties: list[PokemonSpeciesVariety]


@dataclass(frozen=True)
class Genus:
    """Represent a localized genus classification for a Pokémon species.

    Attributes:
        genus (str): The genus label assigned to the Pokémon species, such as `Seed Pokémon`.
        language (NamedAPIResource): The language in which the genus label is written.
    """

    genus: str
    language: NamedAPIResource


@dataclass(frozen=True)
class PokemonSpeciesDexEntry:
    """Represent a Pokédex entry for a Pokémon species.

    Attributes:
        entry_number (int): The index number assigned to the species in the specified Pokédex.
        pokedex (NamedAPIResource): The Pokédex containing this entry.
    """

    entry_number: int
    pokedex: NamedAPIResource


@dataclass(frozen=True)
class PalParkEncounterArea:
    """Represent a Pal Park encounter area for a Pokémon species.

    Attributes:
        base_score (int): The base score awarded when this species is caught during a Pal Park run in the specified
            area.
        rate (int): The base rate at which this species can be encountered in the specified Pal Park area.
        area (NamedAPIResource): The Pal Park area in which this encounter occurs.
    """

    base_score: int
    rate: int
    area: NamedAPIResource


@dataclass(frozen=True)
class PokemonSpeciesVariety:
    """Represent a Pokémon variety associated with a species.

    Attributes:
        is_default (bool): Whether this is the default Pokémon variety for the species.
        pokemon (NamedAPIResource): The Pokémon resource representing this variety.
    """

    is_default: bool
    pokemon: NamedAPIResource
