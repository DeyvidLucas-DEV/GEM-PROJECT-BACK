from sqlalchemy.orm import Session
from app.models import models
from app.schemas.schemas import SubgrupoCreate, IntegranteCreate
import bcrypt

def create_subgrupo(db: Session, subgrupo: SubgrupoCreate):
    db_subgrupo = models.Subgrupo(nome_subgrupo=subgrupo.nome_subgrupo)
    db.add(db_subgrupo)
    db.commit()
    db.refresh(db_subgrupo)
    return db_subgrupo

def get_subgrupos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Subgrupo).offset(skip).limit(limit).all()

def create_integrante(db: Session, integrante: IntegranteCreate):
    hashed_password = bcrypt.hashpw(
        integrante.password.encode(), bcrypt.gensalt()
    ).decode()
    db_integrante = models.Integrante(
        nome_integrante=integrante.nome_integrante,
        e_mail_integrante=integrante.e_mail_integrante,
        password=hashed_password,
        id_subgrupo=integrante.id_subgrupo,
    )
    db.add(db_integrante)
    db.commit()
    db.refresh(db_integrante)
    return db_integrante

def get_integrantes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Integrante).offset(skip).limit(limit).all()
