from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from .. import schemas, models, database, crud, auth

router = APIRouter()


@router.post("/signup", response_model=schemas.Token)
def signup(user_in: schemas.UserCreate, session: Session = Depends(database.get_session)):
    # check if email already exists
    if crud.get_user_by_email(session, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    # hash password & create user
    hashed = auth.get_password_hash(user_in.password)
    user = models.User(
        name=user_in.name,
        email=user_in.email,
        hashed_password=hashed,
        role=user_in.role,
    )
    user = crud.create_user(session, user)

    # issue JWT token
    access_token = auth.create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login", response_model=schemas.Token)
def login(form_data: schemas.UserCreate, session: Session = Depends(database.get_session)):
    # check user
    user = crud.get_user_by_email(session, form_data.email)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    if not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    # issue JWT token
    access_token = auth.create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
