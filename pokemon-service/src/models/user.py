from pydantic import BaseModel, Field, EmailStr


class UserModel(BaseModel):
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "Enrique Velasco Jimenez",
                "email": "enrique.velasco@gmail.com",
                "password": "password1234$"
            }
        }