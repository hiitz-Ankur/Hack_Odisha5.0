from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from datetime import date
from .. import database, schemas, models, crud, auth

router = APIRouter()

@router.post("/", response_model=schemas.ContractRead)
def create_contract(contract_in: schemas.ContractCreate, session: Session = Depends(database.get_session), current_user: models.User = Depends(auth.get_current_user)):
    # only hirer can create contract
    if current_user.role != "hirer":
        raise HTTPException(status_code=403, detail="Only hirers can create contracts")
    job = crud.get_job(session, contract_in.job_id)
    if not job or job.hirer_id != current_user.id:
        raise HTTPException(status_code=404, detail="Job not found or not yours")
    # create contract
    contract = models.Contract(
        job_id=contract_in.job_id,
        hirer_id=current_user.id,
        freelancer_id=contract_in.freelancer_id,
        start_date=contract_in.start_date or date.today(),
        end_date=contract_in.end_date,
        status="active"
    )
    saved = crud.create_contract(session, contract)
    # close job
    job.status = "closed"
    session.add(job)
    # mark accepted application (if exists)
    apps = crud.list_applications_for_job(session, job.id)
    for a in apps:
        if a.freelancer_id == contract_in.freelancer_id:
            a.status = "accepted"
            session.add(a)
        else:
            if a.status == "pending":
                a.status = "rejected"
                session.add(a)
    # set freelancer availability false if profile exists
    from .. import models as _models
    profile = session.exec(select(_models.FreelancerProfile).where(_models.FreelancerProfile.user_id == contract_in.freelancer_id)).first()
    if profile:
        profile.availability = False
        session.add(profile)
    session.commit()
    session.refresh(saved)
    return saved

@router.get("/", response_model=list[schemas.ContractRead])
def list_my_contracts(session: Session = Depends(database.get_session), current_user: models.User = Depends(auth.get_current_user)):
    return crud.list_contracts_for_user(session, current_user.id)
