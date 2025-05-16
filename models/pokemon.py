from models.pokemon_type import PokemonType
from traits.json_trait import JsonTrait

from dataclasses import dataclass


@dataclass(frozen=True)
class Pokemon(JsonTrait):
    id: str
    name: str
    category: str
    entry: str
    generation: int
    types: list[PokemonType]
    weaknesses: list[PokemonType]
