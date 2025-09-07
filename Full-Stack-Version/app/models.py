from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    hashed_password: str
    role: str  # "freelancer" or "hirer"

class FreelancerProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    skills: Optional[str] = None
    experience: Optional[int] = 0
    availability: bool = True

class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hirer_id: int = Field(foreign_key="user.id")
    title: str
    description: Optional[str] = None
    required_skill: Optional[str] = None
    status: str = "open"  # open, closed

class Application(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    job_id: int = Field(foreign_key="job.id")
    freelancer_id: int = Field(foreign_key="user.id")
    proposal: Optional[str] = None
    status: str = "pending"  # pending, accepted, rejected

class Contract(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    job_id: int = Field(foreign_key="job.id")
    hirer_id: int = Field(foreign_key="user.id")
    freelancer_id: int = Field(foreign_key="user.id")
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: str = "active"  # active, completed, cancelled

class Feedback(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    contract_id: int = Field(foreign_key="contract.id")
    rating: Optional[int] = None
    review: Optional[str] = None
