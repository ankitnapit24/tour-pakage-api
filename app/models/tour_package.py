from sqlalchemy import Boolean, Integer, Numeric, String, Text, JSON
from sqlalchemy.orm import mapped_column
from app.database import Base


class TourPackage(Base):
    __tablename__ = "tour_packages"

    id = mapped_column(Integer, primary_key=True, index=True)
    package_name = mapped_column(String(150), nullable=False)
    destination = mapped_column(String(150), nullable=False)
    description = mapped_column(Text, nullable=False)
    duration = mapped_column(Integer, nullable=False)
    price = mapped_column(Numeric(10, 2), nullable=False)
    category = mapped_column(String(100), nullable=False)
    itinerary = mapped_column(JSON, nullable=False)
    inclusions = mapped_column(JSON, nullable=False)
    exclusions = mapped_column(JSON, nullable=False)
    images = mapped_column(JSON, nullable=False)
    availability = mapped_column(Boolean, default=True, nullable=False)
    is_active = mapped_column(Boolean, default=True, nullable=False)