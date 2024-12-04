from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.auth.auth import (
    create_access_token
)

from server.helpers.user import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)
from server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema
)

router = APIRouter()

@router.post("/", response_description="User data added")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    token = create_access_token({'name': user['name'],'lastname': user['last_name'], 'rol': user['rol']})
    response = {'"access_token"': token, 'data': new_user }
    return ResponseModel(response, "User created")

@router.get("/", response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "Users successfully retrieved")
    return ResponseModel(users, "No users retrieved")


@router.get("/{id}", response_description="User retrieved")
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "User successfully retrieved")
    return ErrorResponseModel("Error", 400, "User does not exist")

@router.put("/{id}", response_description="User edited")
async def update_user_data(id: str, req: UserSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            updated_user, "User successfully edited"
        )
    return ErrorResponseModel(
        "Error",
        400,
        "It was an error at updating",
    )

@router.delete("/{id}", response_description="User deleted")
async def delete_socie_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            deleted_user, "User successfully deleted"
        )
    return ErrorResponseModel(
        "Error", 400, "It was an error at deleting"
    )