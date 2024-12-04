from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer 
from server.auth.auth_bearer import JWTBearer
from server.helpers.rol import (
    retrieve_films,
    retrieve_vehicles,
    retrieve_locations,
    retrieve_people,
    retrieve_species
)
from server.models.rol import (
    ResponseModel
)

router = APIRouter()
security = HTTPBearer()

@router.get("/films", dependencies=[Depends(JWTBearer('Films'))])
def get_films():
    films = retrieve_films()
    if films:
       return ResponseModel(films, "Films successfully retrieved")
    return ResponseModel(films, "No films retrieved")
    
    
@router.get("/locations",  dependencies=[Depends(JWTBearer('Locations'))])
async def get_locations():
    locations = retrieve_locations()
    if locations:
        return ResponseModel(locations, "Locations successfully retrieved")
    return ResponseModel(locations, "No locations retrieved")
    

@router.get("/people",  dependencies=[Depends(JWTBearer('People'))])
async def get_people():
    people = retrieve_people()
    if people:
        return ResponseModel(people, "People successfully retrieved")
    return ResponseModel(people, "No people retrieved")
    

@router.get("/species",  dependencies=[Depends(JWTBearer('Species'))])
async def get_species():
    species = retrieve_species()
    if species:
        return ResponseModel(species, "Species successfully retrieved")
    return ResponseModel(species, "No species retrieved")
    
@router.get("/vehicles",  dependencies=[Depends(JWTBearer('Vehicles'))])
async def get_vehicles():
    vehicles = retrieve_vehicles()
    if vehicles:
        return ResponseModel(vehicles, "Vehicles successfully retrieved")
    return ResponseModel(vehicles, "No vehicles retrieved")
    