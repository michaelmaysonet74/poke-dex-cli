from clients.models.pokemon_response import PokemonResponse, PokemonTypeResponse
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

    def _parse_response(self, json_data: PokemonResponse) -> Pokemon | None:
        try:
            return Pokemon(
                id=json_data["id"],
                name=json_data["name"],
                category=json_data["category"],
                entry=json_data["entry"],
                generation=json_data["generation"],
                types=self._convert_types(json_data["types"]),
                weaknesses=self._convert_weaknesses(json_data["weaknesses"]),
            )
        except:
            return None

    def _convert_types(self, types: PokemonTypeResponse) -> list[PokemonType]:
        primary_type: str = types["primary"]
        secondary_type: str | None = types["secondary"]
        return [PokemonType(t) for t in [primary_type, secondary_type] if t]

    def _convert_weaknesses(self, weaknesses: list[str]) -> list[PokemonType]:
        return [PokemonType(type_name) for type_name in weaknesses]
