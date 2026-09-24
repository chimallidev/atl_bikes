from app.infrastructure.models.catalog import (
    BrandModel,
    CategoryModel,
    ProductModel,
)
from app.infrastructure.repositories.product_repository import SQLAlchemyProductRepository
from decimal import Decimal

def test_get_by_ids_returns_products(
    test_db_session,
):
    brand = BrandModel(
        id=1,
        name="Trek",
        slug="trek",
        logo_url=None,
    )

    category = CategoryModel(
        id=1,
        name="Ruta",
        slug="ruta",
        image_url=None,
    )

    product_1 = ProductModel(
        id=1,
        name="Bike One",
        slug="bike-one",
        current_price=Decimal("10000.00"),
        compare_at_price=Decimal("12000.00"),
        is_featured=False,
        brand_id=1,
        category_id=1,
    )

    product_2 = ProductModel(
        id=2,
        name="Bike Two",
        slug="bike-two",
        current_price=Decimal("20000.00"),
        compare_at_price=None,
        is_featured=True,
        brand_id=1,
        category_id=1,
    )

    test_db_session.add_all([
        brand,
        category,
        product_1,
        product_2,
    ])

    test_db_session.commit()

    repository = SQLAlchemyProductRepository(
        session=test_db_session,
    )

    result = repository.get_by_ids(
        product_ids=[1, 2],
    )

    assert len(result) == 2

    assert result[0].id == 1
    assert result[0].name == "Bike One"

    assert result[1].id == 2
    assert result[1].name == "Bike Two"

def test_get_by_ids_returns_empty_list_when_products_do_not_exist(
    test_db_session,
):
    repository = SQLAlchemyProductRepository(
        session=test_db_session,
    )

    result = repository.get_by_ids(
        product_ids=[999, 1000],
    )

    assert result == []

def test_get_by_ids_returns_empty_list_when_ids_are_empty(
    test_db_session,
):
    repository = SQLAlchemyProductRepository(
        session=test_db_session,
    )

    result = repository.get_by_ids(
        product_ids=[],
    )

    assert result == []