# ElTholasy Hospital

A hospital appointment system. Patients can see clinics and doctors and book an appointment. Staff manage doctors, clinics, patients and bookings.

## Features
- Clinics and doctors list (read and manage)
- Appointment booking with checks: no double booking for the same doctor and time, maximum 20 bookings per day
- Patients and user accounts management
- REST API built with Django REST Framework
- React frontend (Vite) with pages: Home, Clinics, Doctors, Doctor details, Appointments, Patients

## Tech stack
Python, Django, Django REST Framework, MySQL, React, Vite

## Project structure

backend/    Django project (apps: accounts, clinics, doctors, patients, appointments, services)
frontend/   React app


## Run the backend
bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django djangorestframework django-cors-headers mysqlclient
# create backend/.env with the values from the Settings section below
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

The project uses MySQL. Create an empty database named eltholasy_hospital first.

## Run the frontend
bash
cd frontend
npm install
npm run dev

Open http://localhost:5173 (the backend runs on http://127.0.0.1:8000).

## Settings
Set in backend/.env: DJANGO_SECRET_KEY, DJANGO_DEBUG, DJANGO_ALLOWED_HOSTS, DJANGO_CORS_ALLOWED_ORIGINS and the DB_* values. Never commit the .env file.

Example backend/.env:

DJANGO_SECRET_KEY=change-me-to-a-long-random-string
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=eltholasy_hospital
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=127.0.0.1
DB_PORT=3306
