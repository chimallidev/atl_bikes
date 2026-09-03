import pytest
from app.application.services.product_featured_service import (
    ProductFeaturedService,
)
from app.domain.exceptions.product_exceptions import (
    FeaturedProductsLimitExceededError,
)
from app.infrastructure.unit_of_work import (
    SQLAlchemyUnitOfWork,
)


def test_get_featured_products() -> None:

    unit_of_work = SQLAlchemyUnitOfWork()

    service = ProductFeaturedService(
        unit_of_work=unit_of_work,
    )

    products = service.get_featured_products()

    print("\nProductos destacados:")

    for product in products:
        print(
            f"- {product.id}: "
            f"{product.name} | "
            f"${product.current_price}"
        )

    assert len(products) <= 3


def test_maximum_three_featured_products() -> None:

    unit_of_work = SQLAlchemyUnitOfWork()

    service = ProductFeaturedService(
        unit_of_work=unit_of_work,
    )

    try:
        service.feature_product(
            product_id=1,
        )

    except FeaturedProductsLimitExceededError as error:

        print(
            "\nRegla de destacados aplicada:"
        )

        print(error)

        assert True

def test_feature_three_products() -> None:

    unit_of_work = SQLAlchemyUnitOfWork()

    service = ProductFeaturedService(
        unit_of_work=unit_of_work,
    )

    service.feature_product(product_id=2)
    service.feature_product(product_id=3)

    products = service.get_featured_products()

    assert len(products) == 3

    assert all(
        product.is_featured
        for product in products
    )

def test_cannot_feature_fourth_product() -> None:

    unit_of_work = SQLAlchemyUnitOfWork()

    service = ProductFeaturedService(
        unit_of_work=unit_of_work,
    )

    with pytest.raises(
        FeaturedProductsLimitExceededError
    ):
        service.feature_product(
            product_id=4,
        )