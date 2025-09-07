from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from .. import database, schemas, models, crud, auth

router = APIRouter()

@router.post("/", response_model=schemas.JobRead)
def create_job(job_in: schemas.JobCreate, session: Session = Depends(database.get_session), current_user: models.User = Depends(auth.get_current_user)):
    # only hirers can post jobs
    if current_user.role != "hirer":
        raise HTTPException(status_code=403, detail="Only hirers can create jobs")
    job = models.Job(hirer_id=current_user.id, title=job_in.title, description=job_in.description, required_skill=job_in.required_skill)
    return crud.create_job(session, job)

@router.get("/", response_model=list[schemas.JobRead])
def list_jobs(session: Session = Depends(database.get_session)):
    return crud.list_jobs(session)

@router.get("/{job_id}", response_model=schemas.JobRead)
def get_job(job_id: int, session: Session = Depends(database.get_session)):
    job = crud.get_job(session, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
