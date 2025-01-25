import urllib3
import json

from database import pokemon_collection

def pokemon_casting(pokemon) -> dict:
    return {
        "id": str(pokemon["_id"]),
        "id_api": pokemon["id_api"],
        "name": pokemon["name"],
        "height": pokemon["height"],
        "weight": pokemon["weight"]
    }

def retrieve_pokemons():
    pokemons = urllib3.request("GET",'https://pokeapi.co/api/v2/pokemon/?limit=10')
    pokemons_decoded = pokemons.data.decode('utf-8')
    pokemons_json = json.loads(pokemons_decoded)
    return pokemons_json['results']
def retrieve_pokemon(id):
    pokemon = urllib3.request("GET",f'https://pokeapi.co/api/v2/pokemon/{id}')
    pokemon_decoded = pokemon.data.decode('utf-8')
    pokemon_json = json.loads(pokemon_decoded)
    return pokemon_json
async def retrieve_internal_pokemons():
    pokemons = []
    async for pokemon in pokemon_collection.find():
        pokemons.append(pokemon_casting(pokemon))
    return pokemons

async def add_pokemon(pokemon_data: dict) -> dict:
    
    pokemon = await pokemon_collection.insert_one(pokemon_data)
    new_pokemon = await pokemon_collection.find_one({"_id": pokemon.inserted_id})
    return pokemon_casting(new_pokemon)

async def retrieve_internal_pokemon(id): # Validate if a pokemon exists in the internal DB
    pokemon = await pokemon_collection.find_one({"id_api": int(id)})
    if pokemon:
        return pokemon_casting(pokemon)
    return None

 