from models.pokemon import Pokemon, PokemonId

from rich.console import Console
from rich.table import Table


console: Console = Console()


def pretty_print(pokemon: Pokemon) -> None:
    table = Table(f"{pokemon.name} {pretty_id(pokemon.id)}", width=85)

    table.add_row(f"[italic]{pokemon.entry}[/italic]")
    table.add_section()

    table.add_row(f"[bold]Category:[/bold] {pokemon.category}")
    table.add_section()

    table.add_row(f"[bold]Types:[/bold] {" | ".join(pokemon.types)}")
    table.add_section()

    table.add_row(f"[bold]Weaknesses:[/bold] {" | ".join(pokemon.weaknesses)}")

    console.print(table)


def pretty_id(pokemon_id: PokemonId) -> str:
    match int(pokemon_id):
        case id if id < 10:
            return f"#000{id}"
        case id if id < 100:
            return f"#00{id}"
        case id if id < 1000:
            return f"#0{id}"
        case _:
            return f"#{pokemon_id}"
