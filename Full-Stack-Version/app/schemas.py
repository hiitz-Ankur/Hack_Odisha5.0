from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

# Auth
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str  # "freelancer" or "hirer"

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None

# Profile
class ProfileCreate(BaseModel):
    skills: Optional[str] = None
    experience: Optional[int] = 0
    availability: Optional[bool] = True

class ProfileRead(ProfileCreate):
    id: int
    user_id: int

# Job
class JobCreate(BaseModel):
    title: str
    description: Optional[str] = None
    required_skill: Optional[str] = None

class JobRead(JobCreate):
    id: int
    hirer_id: int
    status: str

# Application
class ApplicationCreate(BaseModel):
    job_id: int
    proposal: Optional[str] = None

class ApplicationRead(BaseModel):
    id: int
    job_id: int
    freelancer_id: int
    proposal: Optional[str]
    status: str

# Contract
class ContractCreate(BaseModel):
    job_id: int
    freelancer_id: int
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class ContractRead(BaseModel):
    id: int
    job_id: int
    hirer_id: int
    freelancer_id: int
    start_date: Optional[date]
    end_date: Optional[date]
    status: str

# Feedback
class FeedbackCreate(BaseModel):
    contract_id: int
    rating: int
    review: Optional[str] = None

class FeedbackRead(BaseModel):
    id: int
    contract_id: int
    rating: int
    review: Optional[str]
