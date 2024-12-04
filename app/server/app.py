from fastapi import FastAPI
from server.routes.user import router as UserRouter
from server.routes.rol import router as RolRouter

app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(RolRouter, tags=["Rol"], prefix="/rol")
@app.get("/", tags=['root'])
async def read_root():
    return {"message": "Hola Banpay!! Soy Enrique Velasco y esta es mi solución al challenge de backend"}