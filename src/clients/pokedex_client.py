from clients.models.pokemon_response import PokemonResponse

import requests


class PokedexClient:
    def __init__(self, base_url: str, timeout: float | None = 1):
        self.base_url = base_url
        self.timeout = timeout

    def get_pokemon_by_id(self, id: int) -> PokemonResponse | None:
        try:
            response = requests.get(
                f"{self.base_url}/api/v1/pokemon/{id}",
                timeout=self.timeout,
            )
            return response.json() if response.status_code == 200 else None
        except:
            return None

    def get_pokemon_by_name(self, name: str) -> PokemonResponse | None:
        try:
            response = requests.get(
                f"{self.base_url}/api/v1/pokemon",
                {
                    "name": name,
                },
                timeout=self.timeout,
            )
            return response.json() if response.status_code == 200 else None
        except:
            return None
