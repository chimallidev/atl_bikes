from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..infrastructure.database.session import get_db
from ..infrastructure.repositories.product_repository import (
    ProductRepository,
)




router = APIRouter()
ProductResponse = []

@router.get("/db-catalog")
def get_catalog(
    session: Session = Depends(get_db),
) -> list:
    repository = ProductRepository(session)

    products = repository.get_all()

    return products