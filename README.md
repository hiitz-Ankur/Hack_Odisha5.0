# 🏗️ NAUKRI BANDHU – Full-Stack Version

A two-sided marketplace connecting contractors with employees for quick, location-based job placements.  
This platform streamlines the process of finding and hiring temporary labor, making it easy for contractors to post job requirements and for workers to find nearby opportunities.

---

## 🚀 Features

- **Dual User Roles**: Distinct experiences for workers (employees) and contractors (employers).
- **Intuitive Job Search**: Employees can view job listings near their location with details (timings, wages, skills).
- **Accept/Reject Jobs**: Workers can accept or reject jobs directly from the job description page.
- **Efficient Job Posting**: Contractors can post jobs with description, pincode, skills, workers needed, and timeline.
- **Secure Authentication**: Separate login & registration flows for workers and employers.
- **Comprehensive Footer**: Links to key resources for both workers and employers.

---

## 🛠️ Tech Stack

**Backend**
- Python (FastAPI / Flask)
- SQLModel / SQLAlchemy (ORM)

**Database**
- MySQL (or SQLite for dev)
- Alembic (migrations)

**Frontend**
- Jinja2 (templating)
- HTML, CSS, JavaScript

---

## 📂 Project Structure

```bash
Full-Stack-Version/
│
├── alembic/                   # Alembic migration folder
│   ├── versions/              # Holds migration files
│   └── env.py                 # Migration environment config
│
├── alembic.ini                 # Alembic configuration file
│
├── app/                        # Core application
│   ├── __init__.py
│   ├── main.py                 # Entry point (FastAPI app)
│   ├── database.py             # Database connection setup
│   ├── models.py               # ORM models (User, Job, Application)
│   ├── schemas.py              # Pydantic schemas for validation
│   ├── crud.py                 # DB helper functions
│   └── routers/                # All route handlers
│       └── auth_router.py      # Auth routes (login, register)
│
├── templates/                  # Frontend templates
│   ├── base.html               # Common layout
│   ├── home.html
│   ├── employee.html
│   ├── employer.html
│   ├── login_emply.html
│   ├── login_emplyr.html
│   ├── register_emply.html
│   └── register_emplyr.html
│
├── static/                     # Static assets
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── client.js           # Form validation, AJAX
│   │   └── jobs.js             # Job frontend logic
│   └── images/                 # Logos, icons, etc.
│
├── database/                   # Database & migrations
│   ├── schema.sql              # SQL scripts, migrations
│   └── database.db             # SQLite/MySQL DB (dev only)
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
