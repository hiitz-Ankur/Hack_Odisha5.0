from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from .. import database, schemas, models, crud, auth

router = APIRouter()

@router.post("/", response_model=schemas.ApplicationRead)
def apply_to_job(app_in: schemas.ApplicationCreate, session: Session = Depends(database.get_session), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.role != "freelancer":
        raise HTTPException(status_code=403, detail="Only freelancers can apply")
    job = crud.get_job(session, app_in.job_id)
    if not job or job.status != "open":
        raise HTTPException(status_code=400, detail="Job not available")
    application = models.Application(job_id=app_in.job_id, freelancer_id=current_user.id, proposal=app_in.proposal)
    return crud.create_application(session, application)

@router.get("/job/{job_id}")
def list_applications(job_id: int, session: Session = Depends(database.get_session), current_user: models.User = Depends(auth.get_current_user)):
    job = crud.get_job(session, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    # only the hirer who posted the job can see applicants
    if current_user.role != "hirer" or job.hirer_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not permitted to view applications")
    apps = crud.list_applications_for_job(session, job_id)
    return apps
