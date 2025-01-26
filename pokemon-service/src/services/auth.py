import os
import jwt



SECRET_KEY = os.getenv("SECRET_KEY")


def create_access_token(data: dict):
    encoded_jwt = jwt.encode(data, f"{SECRET_KEY}", algorithm="HS256")
    return encoded_jwt

def validate_access_token(token: str):
    try:
    
        decoded_token = jwt.decode(token, f"{SECRET_KEY}", algorithms=["HS256"])
        return decoded_token
    except:
        return {}