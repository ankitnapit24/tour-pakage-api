from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.tour_package import TourPackage
from app.schemas.tour_package import TourPackageCreate


router = APIRouter(prefix="/packages", tags=["Tour Packages"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_package(
    package: TourPackageCreate,
    db: Session = Depends(get_db)
):
    existing_package = db.query(TourPackage).filter(
        TourPackage.package_name == package.package_name,
        TourPackage.destination == package.destination
    ).first()

    if existing_package:
        raise HTTPException(
            status_code=400,
            detail="Tour package already exists"
        )

    new_package = TourPackage(**package.model_dump())

    db.add(new_package)
    db.commit()
    db.refresh(new_package)

    return new_package

@router.get("/")
def search_packages(
    search: str | None = None,
    destination: str | None = None,
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    duration: int | None = None,
    availability: bool | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(TourPackage)

    if search:
        query = query.filter(
            (TourPackage.package_name.ilike(f"%{search}%")) |
            (TourPackage.destination.ilike(f"%{search}%"))
        )

    if destination:
        query = query.filter(
            TourPackage.destination.ilike(f"%{destination}%")
        )

    if category:
        query = query.filter(
            TourPackage.category.ilike(f"%{category}%")
        )

    if min_price is not None:
        query = query.filter(
            TourPackage.price >= min_price
        )

    if max_price is not None:
        query = query.filter(
            TourPackage.price <= max_price
        )

    if duration is not None:
        query = query.filter(
            TourPackage.duration == duration
        )

    if availability is not None:
        query = query.filter(
            TourPackage.availability == availability
        )

    return query.all()




@router.get("/{package_id}")
def get_package(
    package_id: int,
    db: Session = Depends(get_db)
):
    package = db.query(TourPackage).filter(
        TourPackage.id == package_id
    ).first()

    if not package:
        raise HTTPException(
            status_code=404,
            detail="Tour package not found"
        )

    return package


@router.put("/{package_id}")
def update_package(
    package_id: int,
    package: TourPackageCreate,
    db: Session = Depends(get_db)
):
    existing_package = db.query(TourPackage).filter(
        TourPackage.id == package_id
    ).first()

    if not existing_package:
        raise HTTPException(
            status_code=404,
            detail="Tour package not found"
        )

    for key, value in package.model_dump().items():
        setattr(existing_package, key, value)

    db.commit()
    db.refresh(existing_package)

    return existing_package

@router.patch("/{package_id}/deactivate")
def deactivate_package(
    package_id: int,
    db: Session = Depends(get_db)
):
    package = db.query(TourPackage).filter(
        TourPackage.id == package_id
    ).first()

    if not package:
        raise HTTPException(
            status_code=404,
            detail="Tour package not found"
        )

    package.is_active = False

    db.commit()
    db.refresh(package)

    return {
        "message": "Tour package deactivated successfully",
        "package": package
    }