from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.session import get_db
from ..infrastructure.repositories.product_repository import (
    ProductRepository,
)


router = APIRouter()


@router.get("/db-catalog")
def get_catalog(
    session: Session = Depends(get_db),
):
    repository = ProductRepository(session)

    products = repository.get_all()

    return products