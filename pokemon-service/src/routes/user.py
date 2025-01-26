from fastapi import APIRouter, Body, Depends
from middleware.auth_bearer import JWTBearer
from middleware.auth_bearer import JWTBearer

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

# ------ All endpoints ----------
@router.get("/",  dependencies=[Depends(JWTBearer())])
async def get_users(): # Retrieve all users from DB
    users = await retrieve_users()
    if users:
        return RetrieveResponse(users, "Users successfully retrieved")
    return RetrieveResponse(users, "No users retrieved")

@router.get("/{id}", dependencies=[Depends(JWTBearer())]) #
async def get_user_data(id): # Retrieve a singual user by from DB
    user = await retrieve_user(id)
    if user:
        return RetrieveResponse(user, "User successfully retrieved")
    return ErrorResponse( "User does not exist")

@router.put("/{id}", dependencies=[Depends(JWTBearer())])
async def update_user_data(id: str, req: UserModel = Body(...)): #Update a user by id from DB
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return RetrieveResponse(
            updated_user, "User successfully edited"
        )
    return ErrorResponse("It was an error at updating")

@router.delete("/{id}", dependencies=[Depends(JWTBearer())])
async def delete_socie_data(id: str): #Delete user from DB
    deleted_user = await delete_user(id)
    if deleted_user:
        return RetrieveResponse(
            deleted_user, "User successfully deleted"
        )
    return ErrorResponse("It was an error at deleting")