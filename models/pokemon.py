from models.pokemon_type import PokemonType
from traits.json_trait import JsonTrait

from dataclasses import dataclass
from rich import print


@dataclass(frozen=True)
class Pokemon(JsonTrait):
    id: str
    name: str
    category: str
    entry: str
    generation: int
    types: list[PokemonType]
    weaknesses: list[PokemonType]

    def pretty_print(self) -> None:
        print(f" [bold]{self.name}  #{self.id}[/bold]")
        print(f"  [bold]Types:[/bold] {"|".join(self.types)}")
        print(f"  [bold]Category:[/bold] {self.category}")
        print(f"  [bold]Entry:[/bold] {self.entry}")
        print(f"  [bold]Weaknesses:[/bold] {"|".join(self.weaknesses)}")
