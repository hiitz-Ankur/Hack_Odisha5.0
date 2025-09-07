from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(prefix="/employers", tags=["Employers"])

@router.post("/register", response_model=schemas.EmployerOut)
def register_employer(employer: schemas.EmployerCreate, db: Session = Depends(database.get_db)):
    db_employer = crud.get_employer_by_email(db, email=employer.email)
    if db_employer:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_employer(db=db, employer=employer)
