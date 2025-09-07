from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app import crud, models, schemas, database

router = APIRouter()

# Create a job (Employer only)
@router.post("/", response_model=schemas.JobRead)
def create_job(job: schemas.JobCreate, session: Session = Depends(database.get_session), current_user: models.User = Depends(database.get_current_user)):
    if current_user.role != "employer":
        raise HTTPException(status_code=403, detail="Only employers can post jobs")
    db_job = models.Job.from_orm(job)
    db_job.hirer_id = current_user.id
    db_job.status = "open"
    return crud.create_job(session, db_job)

# List all jobs
@router.get("/", response_model=list[schemas.JobRead])
def list_jobs(session: Session = Depends(database.get_session)):
    return crud.list_jobs(session)

# Get single job
@router.get("/{job_id}", response_model=schemas.JobRead)
def get_job(job_id: int, session: Session = Depends(database.get_session)):
    db_job = crud.get_job(session, job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job
