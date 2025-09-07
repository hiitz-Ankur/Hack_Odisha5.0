from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ✅ Import database setup
from Backend import database  

# ✅ Import your routers
from Backend.app.routers import auth_router   # adjust if router file has different name
# from Backend.app.routers import another_router  # add others here if needed

app = FastAPI()

# ✅ Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Startup event for DB
@app.on_event("startup")
async def on_startup():
    database.create_db_and_tables()

# ✅ Routers
app.include_router(auth_router)

# ✅ Root endpoint
@app.get("/")
async def root():
    return {"message": "Backend is running 🚀"}
