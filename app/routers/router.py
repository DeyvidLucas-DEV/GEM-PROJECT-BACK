from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.dependencies import get_current_user
from app.schemas.schemas import (
    Subgrupo,
    SubgrupoCreate,
    Integrante,
    IntegranteCreate,
)
from app.services import service

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def root():
    return {"message": "Welcome to GEM API"}

@router.post(
    "/subgrupos/create",
    response_model=Subgrupo,
    dependencies=[Depends(get_current_user)],
    tags=["Subgrupos"],
)
def create_subgrupo(
    subgrupo: SubgrupoCreate,
    db: Session = Depends(get_db),
):
    return service.create_subgrupo(db, subgrupo)


@router.get("/subgrupos", response_model=List[Subgrupo], tags=["Subgrupos"])
def read_subgrupos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service.get_subgrupos(db, skip=skip, limit=limit)


@router.get("/subgrupos/{id}", response_model=Subgrupo, tags=["Subgrupos"])
def read_subgrupo(id: int, db: Session = Depends(get_db)):
    return service.get_subgrupo(db, id)


@router.put(
    "/subgrupos/{id}",
    response_model=Subgrupo,
    dependencies=[Depends(get_current_user)],
    tags=["Subgrupos"],
)
def update_subgrupo(id: int, subgrupo: SubgrupoCreate, db: Session = Depends(get_db)):
    return service.update_subgrupo(db, id, subgrupo)


@router.delete(
    "/subgrupos/{id}",
    response_model=Subgrupo,
    dependencies=[Depends(get_current_user)],
    tags=["Subgrupos"],
)
def delete_subgrupo(id: int, db: Session = Depends(get_db)):
    return service.delete_subgrupo(db, id)


@router.post(
    "/integrantes",
    response_model=Integrante,
    dependencies=[Depends(get_current_user)],
    tags=["Integrantes"],
)
def create_integrante(integrante: IntegranteCreate, db: Session = Depends(get_db)):
    return service.create_integrante(db, integrante)


@router.get("/integrantes", response_model=List[Integrante], tags=["Integrantes"])
def read_integrantes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service.get_integrantes(db, skip=skip, limit=limit)


@router.get("/integrantes/{id}", response_model=Integrante, tags=["Integrantes"])
def read_integrante(id: int, db: Session = Depends(get_db)):
    return service.get_integrante(db, id)


@router.put(
    "/integrantes/{id}",
    response_model=Integrante,
    dependencies=[Depends(get_current_user)],
    tags=["Integrantes"],
)
def update_integrante(
    id: int,
    integrante: IntegranteCreate,
    db: Session = Depends(get_db),
):
    return service.update_integrante(db, id, integrante)


@router.delete(
    "/integrantes/{id}",
    response_model=Integrante,
    dependencies=[Depends(get_current_user)],
    tags=["Integrantes"],
)
def delete_integrante(id: int, db: Session = Depends(get_db)):
    return service.delete_integrante(db, id)
