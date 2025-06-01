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

def get_subgrupo(db: Session, subgrupo_id: int):
    return (
        db.query(models.Subgrupo)
        .filter(models.Subgrupo.id_subgrupo == subgrupo_id)
        .first()
    )

def update_subgrupo(db: Session, subgrupo_id: int, subgrupo: SubgrupoCreate):
    db_subgrupo = db.query(models.Subgrupo).filter(models.Subgrupo.id_subgrupo == subgrupo_id).first()
    if db_subgrupo:
        db_subgrupo.nome_subgrupo = subgrupo.nome_subgrupo
        db.commit()
        db.refresh(db_subgrupo)
    return db_subgrupo

def delete_subgrupo(db: Session, subgrupo_id: int):
    db_subgrupo = db.query(models.Subgrupo).filter(models.Subgrupo.id_subgrupo == subgrupo_id).first()
    if db_subgrupo:
        db.delete(db_subgrupo)
        db.commit()
    return db_subgrupo

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

def get_integrante(db: Session, integrante_id: int):
    return (
        db.query(models.Integrante)
        .filter(models.Integrante.id_integrante == integrante_id)
        .first()
    )

def update_integrante(db: Session, integrante_id: int, integrante: IntegranteCreate):
    db_integrante = db.query(models.Integrante).filter(models.Integrante.id_integrante == integrante_id).first()
    if db_integrante:
        hashed_password = bcrypt.hashpw(integrante.password.encode(), bcrypt.gensalt()).decode()
        db_integrante.nome_integrante = integrante.nome_integrante
        db_integrante.e_mail_integrante = integrante.e_mail_integrante
        db_integrante.password = hashed_password
        db_integrante.id_subgrupo = integrante.id_subgrupo
        db.commit()
        db.refresh(db_integrante)
    return db_integrante

def delete_integrante(db: Session, integrante_id: int):
    db_integrante = db.query(models.Integrante).filter(models.Integrante.id_integrante == integrante_id).first()
    if db_integrante:
        db.delete(db_integrante)
        db.commit()
    return db_integrante
