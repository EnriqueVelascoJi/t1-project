from fastapi import FastAPI
from routes.pokemon import router as PokemonRouter
from routes.root import router as RootRouter
from routes.auth import router as AuthRouter
from routes.user import router as UserRouter

app = FastAPI()

app.include_router(RootRouter, tags=["root"])
app.include_router(AuthRouter, tags=["Auth"], prefix="/v1/auth")
app.include_router(UserRouter, tags=["User"], prefix="/v1/user")
app.include_router(PokemonRouter, tags=["Pokemon"], prefix="/v1/pokemon")


