from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from .. import database, schemas, models, crud, auth

router = APIRouter()


@router.get("/me")
def read_current_user(current_user: models.User = Depends(auth.get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role,
    }


@router.put("/profile", response_model=schemas.ProfileRead)
def update_profile(
    profile_in: schemas.ProfileCreate,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(auth.get_current_user),
):
    # only freelancers can have profiles
    if current_user.role != "freelancer":
        raise HTTPException(status_code=403, detail="Only freelancers can update profile")

    profile = models.FreelancerProfile(
        user_id=current_user.id,
        skills=profile_in.skills,
        experience=profile_in.experience,
        availability=profile_in.availability,
    )
    result = crud.create_or_update_profile(session, profile)
    return result


@router.get("/profile")
def get_my_profile(
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(auth.get_current_user),
):
    profile = crud.get_profile_by_user(session, current_user.id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
