from models.pokemon import Pokemon
from models.pokemon_type import PokemonType

import requests


class PokedexClient:
    def __init__(self, base_url="http://localhost:8080"):
        self.base_url = base_url

    def get_pokemon_by_id(self, id) -> Pokemon | None:
        response = requests.get(f"{self.base_url}/api/v1/pokemon/{id}")
        return (
            self._parse_response(response.json())
            if response.status_code == 200
            else None
        )

    def get_pokemon_by_name(self, name) -> Pokemon | None:
        response = requests.get(f"{self.base_url}/api/v1/pokemon", {"name": name})
        return (
            self._parse_response(response.json())
            if response.status_code == 200
            else None
        )

    def _parse_response(self, json_data) -> Pokemon:
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
