from fastapi import FastAPI
from routes.pokemon import router as PokemonRouter
from routes.root import router as RootRouter

app = FastAPI()

app.include_router(RootRouter, tags=["root"])
app.include_router(PokemonRouter, tags=["Pokemon"], prefix="/v1")


