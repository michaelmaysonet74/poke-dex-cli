from typing import TypedDict


class PokemonTypeResponse(TypedDict):
    primary: str
    secondary: str | None  # Secondary type can be None if the Pokémon has only one type


class PokemonResponse(TypedDict):
    id: str
    name: str
    category: str
    entry: str
    generation: int
    types: PokemonTypeResponse
    weaknesses: list[str]
