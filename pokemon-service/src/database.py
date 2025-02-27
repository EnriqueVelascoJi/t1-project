import os
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])

database = client.pokemon

pokemon_collection = database.get_collection("pokemon_collection")
user_collection = database.get_collection("user_collection")

