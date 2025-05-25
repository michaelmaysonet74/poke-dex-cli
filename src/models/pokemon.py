from models.pokemon_type import PokemonType
from traits.json_trait import JsonTrait

from dataclasses import dataclass


type PokemonId = str


@dataclass(frozen=True)
class Pokemon(JsonTrait):
    id: PokemonId
    name: str
    category: str
    entry: str
    generation: int
    types: list[PokemonType]
    weaknesses: list[PokemonType]
