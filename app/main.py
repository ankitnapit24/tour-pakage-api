from fastapi import FastAPI
from sqlalchemy import text

from app.database import Base, engine
from app.models.tour_package import TourPackage
from app.routes.tour_packages import router as tour_package_router


app = FastAPI()

app.include_router(tour_package_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Tour Package API is running"}


@app.get("/db-test")
def database_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": result.scalar()}