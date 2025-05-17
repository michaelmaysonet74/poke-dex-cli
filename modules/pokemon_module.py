from clients.pokedex_client import PokedexClient
from services.pokemon_service import PokemonService

import os
from dotenv import load_dotenv


load_dotenv()

pokedex_base_url = os.getenv("POKEDEX_BASE_URL", "http://localhost:8080")
pokedex_client: PokedexClient = PokedexClient(pokedex_base_url)
pokemon_service: PokemonService = PokemonService(pokedex_client)
