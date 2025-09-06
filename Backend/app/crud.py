from sqlmodel import Session, select
from . import models

# Users
def get_user_by_email(session: Session, email: str):
    statement = select(models.User).where(models.User.email == email)
    return session.exec(statement).first()

def create_user(session: Session, user: models.User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Profiles
def create_or_update_profile(session: Session, profile: models.FreelancerProfile):
    existing = session.exec(select(models.FreelancerProfile).where(models.FreelancerProfile.user_id == profile.user_id)).first()
    if existing:
        existing.skills = profile.skills
        existing.experience = profile.experience
        existing.availability = profile.availability
        session.add(existing)
        session.commit()
        session.refresh(existing)
        return existing
    session.add(profile)
    session.commit()
    session.refresh(profile)
    return profile

def get_profile_by_user(session: Session, user_id: int):
    return session.exec(select(models.FreelancerProfile).where(models.FreelancerProfile.user_id == user_id)).first()

# Jobs
def create_job(session: Session, job: models.Job):
    session.add(job)
    session.commit()
    session.refresh(job)
    return job

def list_jobs(session: Session):
    return session.exec(select(models.Job)).all()

def get_job(session: Session, job_id: int):
    return session.get(models.Job, job_id)

# Applications
def create_application(session: Session, application: models.Application):
    session.add(application)
    session.commit()
    session.refresh(application)
    return application

def list_applications_for_job(session: Session, job_id: int):
    return session.exec(select(models.Application).where(models.Application.job_id == job_id)).all()

# Contracts
def create_contract(session: Session, contract: models.Contract):
    session.add(contract)
    session.commit()
    session.refresh(contract)
    return contract

def get_contract(session: Session, contract_id: int):
    return session.get(models.Contract, contract_id)

def list_contracts_for_user(session: Session, user_id: int):
    stmt = select(models.Contract).where((models.Contract.hirer_id == user_id) | (models.Contract.freelancer_id == user_id))
    return session.exec(stmt).all()

# Feedback
def create_feedback(session: Session, feedback: models.Feedback):
    session.add(feedback)
    session.commit()
    session.refresh(feedback)
    return feedback
