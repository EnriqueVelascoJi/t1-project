from pydantic import BaseModel, Field

class PokemonModel(BaseModel):
    id_api: int
    name: str = Field(min_length=1)
    height: int = Field(gt=0)
    weight: int = Field(gt=0)

    class Config:
        json_schema_extra = {
            'example': {
                'id_api': 1,
                'name': 'bulbasaur',
                'height': 7,
                'weight': 69
            }
        }


