# Job
from datetime import date
from typing import Optional
from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    description: Optional[str] = None
    required_skill: Optional[str] = None
    location: Optional[str] = None
    pincode: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    from_date: Optional[date] = None
    from_time: Optional[str] = None
    to_date: Optional[date] = None
    to_time: Optional[str] = None

class JobRead(JobCreate):
    id: int
    hirer_id: int
    status: str
