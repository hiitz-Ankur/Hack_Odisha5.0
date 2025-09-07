from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from .. import database, schemas, models, crud, auth

router = APIRouter()

@router.post("/", response_model=schemas.FeedbackRead)
def give_feedback(f_in: schemas.FeedbackCreate, session: Session = Depends(database.get_session), current_user: models.User = Depends(auth.get_current_user)):
    # Only hirer of the contract can leave feedback (basic rule)
    contract = crud.get_contract(session, f_in.contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    if current_user.id != contract.hirer_id:
        raise HTTPException(status_code=403, detail="Only the hirer can give feedback")
    feedback = models.Feedback(contract_id=f_in.contract_id, rating=f_in.rating, review=f_in.review)
    saved = crud.create_feedback(session, feedback)
    # optional: mark contract completed
    contract.status = "completed"
    session.add(contract)
    session.commit()
    session.refresh(saved)
    return saved
