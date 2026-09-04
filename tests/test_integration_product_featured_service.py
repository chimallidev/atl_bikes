from decimal import Decimal

from sqlalchemy import select

from app.infrastructure.models.catalog import ProductModel
from app.infrastructure import unit_of_work

from app.application.services.product_featured_service import (
    ProductFeaturedService,
)
from app.infrastructure.repositories.product_repository import (
    SQLAlchemyProductRepository,
)
from app.infrastructure.unit_of_work import SQLAlchemyUnitOfWork
from app.infrastructure.database import session as database_session


def test_get_featured_returns_featured_product(
    test_db_session,
    product_with_images,
    monkeypatch,
):
    product, image_1, image_2 = product_with_images

    product.is_featured = True
    test_db_session.commit()

    products_in_db = test_db_session.execute(
        select(ProductModel)
        .where(ProductModel.is_featured.is_(True))
    ).scalars().all()

    print("\nProductos destacados antes del servicio:")

    for item in products_in_db:
        print(
            f"id={item.id}, "
            f"name={item.name}, "
            f"is_featured={item.is_featured}"
        )

    monkeypatch.setattr(
        unit_of_work,
        "SessionLocal",
        lambda: test_db_session,
    )

    uow = SQLAlchemyUnitOfWork()

    service = ProductFeaturedService(uow)

    response = service.get_featured()

    # ...