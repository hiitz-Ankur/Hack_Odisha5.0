from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import create_db_and_tables
from .routers import (
    auth_router,
    users_router,
    jobs_router,
    applications_router,
    contracts_router,
    feedback_router,
)

# Create FastAPI app
app = FastAPI(title="Freelancer-Hirer Portal API")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (hackathon mode)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Include routers
app.include_router(auth_router.router)
app.include_router(users_router.router)
app.include_router(jobs_router.router)
app.include_router(applications_router.router)
app.include_router(contracts_router.router)
app.include_router(feedback_router.router)

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}
from fastapi.responses import FileResponse
import os

# existing app setup...

# 👇 Add this after all app.include_router(...)
@app.get("/favicon.ico")
async def favicon():
    favicon_path = os.path.join("static", "favicon.ico")
    return FileResponse(favicon_path)
