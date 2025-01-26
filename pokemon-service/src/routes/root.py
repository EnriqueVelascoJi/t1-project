from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/", tags=['root']) # rot url 
def read_root():
    return {
        "status": 200,
        "mesage": "Hola estimado equipo de T1. Mi nombre es Enrique Velasco y esta es mi solución al Examen Técnico",
    }

@router.get("/health", tags=['root']) # Show the status from the Application
def health():
    return {
        "status": 200,
        "mesage": "ok",
    }

