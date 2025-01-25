from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from helpers.auth import (
    create_access_token
)

from services.user import (
    delete_user,
    retrieve_user,
    update_user,
    retrieve_users
)
from helpers.user import (
   ErrorResponse,
   RetrieveResponse
)
from models.user import UserModel
router = APIRouter()

@router.get("/", response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return RetrieveResponse(users, "Users successfully retrieved")
    return RetrieveResponse(users, "No users retrieved")

@router.get("/{id}", response_description="User retrieved")
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return RetrieveResponse(user, "User successfully retrieved")
    return ErrorResponse( "User does not exist")

@router.put("/{id}", response_description="User edited")
async def update_user_data(id: str, req: UserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return RetrieveResponse(
            updated_user, "User successfully edited"
        )
    return ErrorResponse("It was an error at updating")

@router.delete("/{id}", response_description="User deleted")
async def delete_socie_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return RetrieveResponse(
            deleted_user, "User successfully deleted"
        )
    return ErrorResponse("It was an error at deleting")