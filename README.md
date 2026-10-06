# Tour Package Management API

A REST API for managing tour packages using FastAPI and PostgreSQL.

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

## Setup

Create and activate virtual environment:

python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Create a `.env` file and add your PostgreSQL database URL:

DATABASE_URL=postgresql+psycopg2://postgres:<PASSWORD>@localhost:5432/tour_package_db

Run the application:

uvicorn app.main:app --reload

## API Documentation

Open:

http://127.0.0.1:8000/docs

## Main Endpoints

- POST /packages/ - Create a tour package
- GET /packages/ - Search and filter tour packages
- GET /packages/{package_id} - Get a tour package
- PUT /packages/{package_id} - Update a tour package
- PATCH /packages/{package_id}/deactivate - Deactivate a tour package