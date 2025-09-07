class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hirer_id: int = Field(foreign_key="user.id")

    title: str
    description: Optional[str] = None
    required_skill: Optional[str] = None
    status: str = "open"  # open, closed

    location: Optional[str] = None
    pincode: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    from_date: Optional[date] = None
    from_time: Optional[str] = None
    to_date: Optional[date] = None
    to_time: Optional[str] = None
