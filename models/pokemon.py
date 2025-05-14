from traits.json_trait import JsonTrait
from models.pokemon_type import PokemonType
from dataclasses import dataclass


@dataclass(frozen=True)
class Pokemon(JsonTrait):
    id: int
    name: str
    types: list[PokemonType]
    weaknesses: list[PokemonType]
