# 🏗️ NAUKRI BANDHU

A two-sided marketplace connecting contractors with employees for quick, location-based job placements.  
This platform streamlines the process of finding and hiring temporary labor, making it easy for contractors to post job requirements and for workers to find nearby opportunities.

---

## 🚀 Features

- **Dual User Roles**: Distinct experiences for workers (employees) and contractors (employers).
- **Intuitive Job Search**: Employees can easily view job listings near their location with details (timings, wages, skills).
- **Accept/Reject Jobs**: Workers can accept or reject jobs directly from the job description page.
- **Efficient Job Posting**: Contractors can post jobs with description, pincode, skills, workers needed, and timeline.
- **Secure Authentication**: Separate login & registration flows for workers and employers.
- **Comprehensive Footer**: Includes links to key resources for both workers and employers.

---

## 🛠️ Technologies Used

### Backend
- **Python** – Core language  
- **FastAPI / Flask** – API & routing  
- **SQLModel / SQLAlchemy** – ORM for database management  

### Database
- **MySQL** – For storing users, jobs, and applications  

### Frontend
- **Jinja2** – Dynamic templating engine  
- **HTML, CSS, JS** – UI & client-side validation  

---

## 📂 Project Structure

```bash
Full-Stack-Version/
├── app/
│   ├── __init__.py
│   ├── main.py              # Entry point (FastAPI/Flask app)
│   ├── database.py          # Database connection setup
│   ├── models.py            # ORM models (User, Job, Application)
│   ├── schemas.py           # Pydantic schemas for validation
│   ├── crud.py              # DB helper functions
│   ├── routers/             # All route handlers
│   │   └── auth_router.py   # Auth routes (login, register)
│
├── templates/               # Frontend templates
│   ├── base.html            # Common layout
│   ├── home.html
│   ├── employee.html
│   ├── employer.html
│   ├── login_emply.html
│   ├── login_emplyr.html
│   ├── register_emply.html
│   └── register_emplyr.html
│
├── static/                  # Static assets
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── client.js        # Form validation, AJAX
│   │   └── jobs.js          # Job frontend logic
│   └── images/              # Logos, icons, etc.
│
├── database/
│   ├── schema.sql           # SQL scripts, migrations
│   └── database.db          # SQLite/MySQL DB (dev only)
│
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
