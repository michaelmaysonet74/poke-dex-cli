from clients.pokedex_client import PokedexClient
from models.pokemon import Pokemon


class PokemonService:
    def __init__(self, pokedex_client: PokedexClient) -> None:
        self.pokedex_client = pokedex_client

    def get_pokemon_by_id(self, id: int) -> Pokemon | None:
        return self.pokedex_client.get_pokemon_by_id(id)

    def get_pokemon_by_name(self, name: str) -> Pokemon | None:
        return self.pokedex_client.get_pokemon_by_name(name)
