from fastapi import APIRouter, Depends, Body
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
#from server.auth.auth_bearer import JWTBearer
from helpers.user import (
    ErrorResponse,
   RetrieveResponse
)
from services.user import (
    add_user
)
from services.auth import (
    create_access_token,
    validate_access_token
)
from helpers.pokemon import (
    RetrieveResponse,
    ErrorResponse

)
from models.user import UserModel

router = APIRouter()
security = HTTPBearer()



# ------ All endpoints ----------
@router.post("/user/signup") # SignUp user in the DB
async def create_user(user: UserModel = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    token = create_access_token({'full_name': user['full_name'],'email': user['email']})
    response = {'access_token': token, 'data': new_user }
    return RetrieveResponse(response, "User created")



