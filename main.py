from commands.pokemon_command import pokemon_app

from typer import Typer


app = Typer()
app.add_typer(pokemon_app)

if __name__ == "__main__":
    app()
