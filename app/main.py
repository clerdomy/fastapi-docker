from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from . import database, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/atleta/", response_model=schemas.Atleta)
async def create_atleta(atleta: schemas.AtletaCreate, db: Session = Depends(get_db)):
    db_atleta = database.get_atleta_by_cpf(db, cpf=atleta.cpf)
    if db_atleta:
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")
    try:
        return database.create_atleta(db=db, atleta=atleta)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")

@app.get("/atleta/", response_model=Page[schemas.Atleta])
async def read_atletas(
    nome: str = Query(None),
    cpf: str = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(models.Atleta)
    if nome:
        query = query.filter(models.Atleta.nome == nome)
    if cpf:
        query = query.filter(models.Atleta.cpf == cpf)
    atletas = query.offset(skip).limit(limit).all()
    return paginate(atletas)

@app.get("/atleta/all", response_model=Page[schemas.Atleta])
async def get_all_atletas(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    atletas = database.get_atletas(db, skip=skip, limit=limit)
    return paginate(atletas)

add_pagination(app)
