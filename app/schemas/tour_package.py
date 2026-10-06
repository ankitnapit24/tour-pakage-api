from pydantic import BaseModel, Field


class TourPackageCreate(BaseModel):
    package_name: str
    destination: str
    description: str
    duration: int = Field(gt=0)
    price: float = Field(ge=0)
    category: str
    itinerary: list
    inclusions: list
    exclusions: list
    images: list
    availability: bool = True