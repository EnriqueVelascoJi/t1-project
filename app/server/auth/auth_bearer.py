from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .auth import validate_access_token


class JWTBearer(HTTPBearer):
    def __init__(self, rol, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error = auto_error)
        self.rol = rol
        
        

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        is_valid_token: bool = False

        try:
            payload = validate_access_token(jwtoken)
            print(payload)
            
        except:
            payload = None
        if payload:
            print(payload)
            rol_decoded = payload['rol']
            print(rol_decoded)
            if rol_decoded == self.rol or rol_decoded == 'Admin':
                is_valid_token = True
        return is_valid_token