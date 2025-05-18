from helpers.pretty_helper import pretty_print
from modules.pokemon_module import pokemon_service

from typer import Typer
from rich.console import Console


pokemon_app: Typer = Typer(name="pokemon")
err_console: Console = Console(style="bold red")


@pokemon_app.command(name="id")
def get_pokemon_by_id(id: int) -> None:
    if pokemon := pokemon_service.get_pokemon_by_id(id):
        pretty_print(pokemon)
    else:
        err_console.print(f"Pokemon with ID: {id} was not found.")


@pokemon_app.command(name="name")
def get_pokemon_by_name(name: str) -> None:
    if pokemon := pokemon_service.get_pokemon_by_name(name):
        pretty_print(pokemon)
    else:
        err_console.print(f'Pokemon with name: "{name.capitalize()}" was not found.')
