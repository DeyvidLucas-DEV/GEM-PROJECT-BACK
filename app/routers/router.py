from fastapi import APIRouter, Depends
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to GEM API"}

@router.post("/subgrupos/create", dependencies=[Depends(get_current_user)])
def create_subgrupo():
    return {"message": "Subgrupo criado (apenas para admin autenticado)"}
