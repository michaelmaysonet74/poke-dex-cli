from clients.pokedex_client import PokedexClient
from services.pokemon_service import PokemonService

from typer import Typer
from rich import print
from rich.console import Console


pokedex_client: PokedexClient = PokedexClient()
pokemon_service: PokemonService = PokemonService(pokedex_client)

pokemon_app: Typer = Typer(name="pokemon")
err_console: Console = Console(style="bold red")


@pokemon_app.command(name="id")
def get_pokemon_by_id(id: int) -> None:
    if pokemon := pokemon_service.get_pokemon_by_id(id):
        print(pokemon.to_json())
    else:
        err_console.print(f"Pokemon with ID: {id} was not found.")


@pokemon_app.command(name="name")
def get_pokemon_by_name(name: str) -> None:
    if pokemon := pokemon_service.get_pokemon_by_name(name):
        print(pokemon.to_json())
    else:
        err_console.print(f'Pokemon with name: "{name.capitalize()}" was not found.')
