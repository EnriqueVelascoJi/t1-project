from typing import Optional

from pydantic import BaseModel, Field, constr


class UserSchema(BaseModel):
    name: constr(strict=True) = Field(...)
    last_name: constr(strict=True) = Field(...)
    rol: constr(strict=True) = Field(...)

    class config:
        schema_extra = {
            "example": {
                "name": "Enrique",
                "last_name": "Velasco",
                "rol": "Admin"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}