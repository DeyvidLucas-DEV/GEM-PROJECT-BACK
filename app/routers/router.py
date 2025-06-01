from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.dependencies import get_current_user
from app.schemas.schemas import Subgrupo, SubgrupoCreate
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
)
def create_subgrupo(
    subgrupo: SubgrupoCreate,
    db: Session = Depends(get_db),
):
    return service.create_subgrupo(db, subgrupo)
