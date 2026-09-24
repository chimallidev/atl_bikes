from decimal import Decimal
from unittest.mock import patch

from app.application.services.product_bestselling_service import (
    ProductBestsellingService,
)
from app.infrastructure.unit_of_work import SQLAlchemyUnitOfWork


def test_get_bestselling_integration(
    test_db_session,
    bestselling_products,
):
    product_ids = [
        product.id
        for product in bestselling_products
    ]

    with patch(
        "app.infrastructure.unit_of_work.SessionLocal",
        return_value=test_db_session,
    ):
        service = ProductBestsellingService(
            unit_of_work=SQLAlchemyUnitOfWork(),
        )

        result = service.get_bestselling(
            product_ids=product_ids,
        )

    assert len(result) == 8

    assert [
        product.id
        for product in result
    ] == product_ids

    assert result[0].id == bestselling_products[0].id

    assert result[0].name == "Test Bike 1"

    assert result[0].slug == "test-bike-1"

    assert result[0].brand == "Test Brand"

    assert (
        result[0].cover_image_url
        == "https://example.com/image-1.jpg"
    )

    assert result[0].current_price == Decimal(
        "1000.00"
    )

    assert result[0].compare_at_price is None

    assert result[0].is_featured is False