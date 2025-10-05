# my-fullstack-app

Minimal modern fullstack app (React + Flask). This README explains how to run the frontend and backend in development and prepare for production.

## Requirements
- Python 3.11+
- Node 18+

## Backend (Flask)
1. Create a virtual environment and install dependencies:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Set environment variables (example):

```bash
export FLASK_ENV=development
export DATABASE_URL=sqlite:///instance/db.sqlite3
export SECRET_KEY=dev-secret
export JWT_SECRET_KEY=dev-jwt-secret
```

3. Run the app locally:

```bash
python run.py
```

Production (Gunicorn) example:

```bash
gunicorn --chdir backend wsgi:application
```

## Frontend (Vite + React)
1. Install dependencies and run:

```bash
cd frontend
npm install
npm run dev
```

2. The Vite dev server proxies `/api` requests to `http://127.0.0.1:5555` (configured in `vite.config.js`).

## Notes
- Blueprints live in `backend/routes/`.
- Use Flask-Migrate for DB migrations (`flask db init/migrate/upgrade`).
# my-fullstack-app
