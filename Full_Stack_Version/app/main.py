from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request  # Needed for passing the request to templates
import os

# ✅ Import database setup
from app import database  

# ✅ Import your routers
from app.routers import (
    applications_router,
    auth_router,
    contracts_router,
    feedback_router,
    jobs_router,
    users_router,
)

app = FastAPI()

current_dir = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(current_dir, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(current_dir, "templates"))


@app.get("/employee")
async def employee_page(request: Request):
    return templates.TemplateResponse("employee.html", {"request": request})

@app.get("/employer")
async def employer_page(request: Request):
    return templates.TemplateResponse("employer.html", {"request": request})

@app.get("/home")
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/employee_login")
async def employee_login_page(request: Request):
    return templates.TemplateResponse("login_emply.html", {"request": request})

@app.get("/employer_login")
async def employer_login_page(request: Request):
    return templates.TemplateResponse("login_emplyr.html", {"request": request})


@app.get("/employee_register")
async def employee_register_page(request: Request):
    return templates.TemplateResponse("register_emply.html", {"request": request})

@app.get("/employer_register")
async def employer_register_page(request: Request):
    return templates.TemplateResponse("register_emplyr.html", {"request": request})


# ✅ Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Change to specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Startup event for DB
@app.on_event("startup")
async def on_startup():
    database.create_db_and_tables()

# ✅ Routers (make sure each file has `router = APIRouter()`)
app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
app.include_router(applications_router.router, prefix="/applications", tags=["Applications"])
app.include_router(contracts_router.router, prefix="/contracts", tags=["Contracts"])
app.include_router(feedback_router.router, prefix="/feedback", tags=["Feedback"])
app.include_router(jobs_router.router, prefix="/jobs", tags=["Jobs"])
app.include_router(users_router.router, prefix="/users", tags=["Users"])

# ✅ Root endpoint
@app.get("/")
async def root():
    return {"message": "Backend is running 🚀"}
