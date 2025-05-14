from models.pokemon import Pokemon, PokemonType
from typer import Typer
from rich import print
from rich.console import Console

POKEMON_LIST = [
    Pokemon(
        id=1,
        name="Bulbasaur",
        types=[PokemonType.GRASS, PokemonType.POISON],
        weaknesses=[
            PokemonType.FIRE,
            PokemonType.FLYING,
            PokemonType.ICE,
            PokemonType.PSYCHIC,
        ],
    ),
    Pokemon(
        id=25,
        name="Pikachu",
        types=[PokemonType.ELECTRIC],
        weaknesses=[PokemonType.GROUND],
    ),
]

pokemon_app: Typer = Typer(name="pokemon")
err_console: Console = Console(style="bold red")


@pokemon_app.command(name="id")
def get_pokemon_by_id(id: int) -> None:
    for pkmn in POKEMON_LIST:
        if pkmn.id == id:
            print(pkmn.to_json())
            return

    err_console.print(f"Pokemon with ID: {id} was not found.")


@pokemon_app.command(name="name")
def get_pokemon_by_name(name: str) -> None:
    for pkmn in POKEMON_LIST:
        if pkmn.name.lower() == name.lower():
            print(pkmn.to_json())
            return

    err_console.print(f'Pokemon with name: "{name.capitalize()}" was not found.')
