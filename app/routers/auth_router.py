from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.database import SessionLocal
from app.schemas.schemas import Token
from app.services import auth_service
from app.models import models
import bcrypt

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_admin = db.query(models.Integrante).filter(
        models.Integrante.e_mail_integrante == form_data.username
    ).first()
    if not db_admin or not bcrypt.checkpw(form_data.password.encode(), db_admin.password.encode()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    if db_admin.id_subgrupo != 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not an admin user")
    access_token = auth_service.create_access_token(data={"sub": db_admin.e_mail_integrante})
    return {"access_token": access_token, "token_type": "bearer"}
