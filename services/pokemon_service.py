from clients.pokedex_client import PokedexClient
from models.pokemon import Pokemon
from models.pokemon_type import PokemonType


class PokemonService:
    def __init__(self, pokedex_client: PokedexClient) -> None:
        self.pokedex_client = pokedex_client

    def get_pokemon_by_id(self, id: int) -> Pokemon | None:
        maybe_response = self.pokedex_client.get_pokemon_by_id(id)
        return self._parse_response(maybe_response) if maybe_response else None

    def get_pokemon_by_name(self, name: str) -> Pokemon | None:
        maybe_response = self.pokedex_client.get_pokemon_by_name(name)
        return self._parse_response(maybe_response) if maybe_response else None

    def _parse_response(self, json_data: dict) -> Pokemon:
        return Pokemon(
            id=json_data["id"],
            name=json_data["name"],
            category=json_data["category"],
            entry=json_data["entry"],
            generation=json_data["generation"],
            types=[
                PokemonType(t)
                for t in [
                    json_data["types"]["primary"],
                    json_data["types"]["secondary"],
                ]
                if t
            ],
            weaknesses=json_data["weaknesses"],
        )
