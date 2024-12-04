import urllib3
import json

def retrieve_films():
    films = urllib3.request("GET",'https://ghibliapi.vercel.app/films')
    films_decoded = films.data.decode('utf-8')
    films_json = json.loads(films_decoded)
    return films_json

def retrieve_people():
    people = urllib3.request("GET",'https://ghibliapi.vercel.app/people')
    people_decoded = people.data.decode('utf-8')
    people_json = json.loads(people_decoded)
    return people_json

def retrieve_locations():
    locations = urllib3.request("GET",'https://ghibliapi.vercel.app/locations')
    locations_decoded = locations.data.decode('utf-8')
    locations_json = json.loads(locations_decoded)
    return locations_json

def retrieve_species():
    species = urllib3.request("GET",'https://ghibliapi.vercel.app/species')
    species_decoded = species.data.decode('utf-8')
    species_json = json.loads(species_decoded)
    return species_json

def retrieve_vehicles():
    vehicles = urllib3.request("GET",'https://ghibliapi.vercel.app/vehicles')
    vehicles_decoded = vehicles.data.decode('utf-8')
    vehicles_json = json.loads(vehicles_decoded)
    return vehicles_json
