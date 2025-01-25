from fastapi import APIRouter, Depends, Body
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
#from server.auth.auth_bearer import JWTBearer
from services.pokemon import (
    retrieve_pokemons,
    retrieve_pokemon,
    retrieve_internal_pokemons,
    retrieve_internal_pokemon,
    add_pokemon
)
from helpers.pokemon import (
    validate_id,
    RetrieveResponse,
    ErrorResponse

)
from models.pokemon import PokemonModel

router = APIRouter()
security = HTTPBearer()



# ------ All endpoints ----------
@router.get("/pokemons") #Retrieve data from external API
async def get_pokemons():
    try:
        pokemons = retrieve_pokemons() ## Call the retrieve pokemons service
        if pokemons:
            return RetrieveResponse(pokemons, "Retrive pokemons successfully")

        return ErrorResponse("No service available")
    except:
        return ErrorResponse("No service available")

@router.get("/pokemons/internal") #Retrieve data from the internal DB
async def get_pokemons():
    try:
        pokemons = await retrieve_internal_pokemons() ## Call the retrieve pokemons service
        if pokemons:
            return RetrieveResponse(pokemons, "Retrive pokemons successfully")

        return ErrorResponse("No service available")
    except: 
        return ErrorResponse("No service available")


@router.get("/pokemon/{id}") #Retrieve a pokemon by id. If not exists saves it in the ineternal DB
async def get_pokemon(id):
    if(not validate_id(id)): # Validate the id beteween 1 and 10
        return ErrorResponse("Invalid ID. It needs to be beteween 1 and 10") 
    
    try:
        pokemon = retrieve_pokemon(id) # Call the retrieve pokemon by id service from the external api
        
        internal_pokemon = await retrieve_internal_pokemon(id) # Retreive a internal pokemon from DB
        print(internal_pokemon)
        if internal_pokemon is not None: # Validate if a pokemon exists in the inetrnal DB
            return RetrieveResponse(internal_pokemon, "Retrieve pokemon by id successfully")

        else:
            pokemon_data = PokemonModel(
                id_api = pokemon['id'],
                name = pokemon['name'],
                height = pokemon['height'],
                weight = pokemon['weight']
            )
            pokemon_json = jsonable_encoder(pokemon_data)
            new_pokemon = await add_pokemon(pokemon_json)
            return RetrieveResponse(new_pokemon, "Save and retrieve pokemon by id successfully")

    except:
        return ErrorResponse("No service available")

    
