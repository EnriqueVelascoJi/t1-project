from  server.database import user_collection
from bson.objectid import ObjectId


def user_casting(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "last_name": user["last_name"],
        "rol": user["rol"]
    }

async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_casting(user))
    return users

async def add_user(user_data: dict, ) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_casting(new_user)

async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_casting(user)


async def update_user(id: str, data: dict):
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False

async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True
