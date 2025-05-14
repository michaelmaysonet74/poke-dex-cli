from typer import Typer
from commands.pokemon import pokemon_app

app = Typer()
app.add_typer(pokemon_app)

if __name__ == "__main__":
    app()
