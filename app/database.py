from sqlalchemy.orm import Session

from . import models, schemas
from .models import Atleta, SessionLocal, engine


def get_atleta_by_cpf(db: Session, cpf: str):
    return db.query(models.Atleta).filter(models.Atleta.cpf == cpf).first()

def get_atletas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Atleta).offset(skip).limit(limit).all()

def create_atleta(db: Session, atleta: schemas.AtletaCreate):
    db_atleta = models.Atleta(**atleta.dict())
    db.add(db_atleta)
    db.commit()
    db.refresh(db_atleta)
    return db_atleta
