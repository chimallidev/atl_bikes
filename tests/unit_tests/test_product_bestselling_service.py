from decimal import Decimal
from unittest.mock import MagicMock

from app.application.schemas.product_schema import (
    BestsellingProductResponse,
)
from app.application.services.product_bestselling_service import (
    ProductBestsellingService,
)
from app.domain.entities.brand import Brand
from app.domain.entities.product import Product
from app.domain.entities.product_image import ProductImage


def create_product(
    product_id: int,
    name: str,
    slug: str,
    brand_name: str,
    cover_image_url: str,
) -> Product:

    brand = Brand(
        id=product_id,
        name=brand_name,
        slug=brand_name.lower(),
        logo_url=None,
    )

    image = ProductImage(
        id=product_id,
        product_id=product_id,
        image_url=cover_image_url,
        is_cover=True,
    )

    return Product(
        id=product_id,
        name=name,
        slug=slug,
        brand_id=product_id,
        brand=brand,
        category_id=None,
        images=[image],
        current_price=Decimal("10000.00"),
        compare_at_price=Decimal("12000.00"),
        is_featured=False,
    )


def test_get_bestselling_returns_products():

    product_1 = create_product(
        product_id=1,
        name="Bike One",
        slug="bike-one",
        brand_name="Trek",
        cover_image_url="https://example.com/bike-one.jpg",
    )

    product_2 = create_product(
        product_id=2,
        name="Bike Two",
        slug="bike-two",
        brand_name="Specialized",
        cover_image_url="https://example.com/bike-two.jpg",
    )

    unit_of_work = MagicMock()

    unit_of_work.__enter__.return_value = unit_of_work
    unit_of_work.products.get_by_ids.return_value = [
        product_1,
        product_2,
    ]

    service = ProductBestsellingService(
        unit_of_work=unit_of_work,
    )

    result = service.get_bestselling(
        product_ids=[1, 2],
    )

    assert result == [
        BestsellingProductResponse(
            id=1,
            name="Bike One",
            slug="bike-one",
            brand="Trek",
            cover_image_url="https://example.com/bike-one.jpg",
            current_price=Decimal("10000.00"),
            compare_at_price=Decimal("12000.00"),
            is_featured=False,
        ),
        BestsellingProductResponse(
            id=2,
            name="Bike Two",
            slug="bike-two",
            brand="Specialized",
            cover_image_url="https://example.com/bike-two.jpg",
            current_price=Decimal("10000.00"),
            compare_at_price=Decimal("12000.00"),
            is_featured=False,
        ),
    ]

    unit_of_work.products.get_by_ids.assert_called_once_with(
        product_ids=[1, 2],
    )

def test_get_bestselling_preserves_requested_order():

    product_1 = create_product(
        product_id=1,
        name="Bike One",
        slug="bike-one",
        brand_name="Trek",
        cover_image_url="https://example.com/1.jpg",
    )

    product_2 = create_product(
        product_id=2,
        name="Bike Two",
        slug="bike-two",
        brand_name="Specialized",
        cover_image_url="https://example.com/2.jpg",
    )

    product_3 = create_product(
        product_id=3,
        name="Bike Three",
        slug="bike-three",
        brand_name="Cannondale",
        cover_image_url="https://example.com/3.jpg",
    )

    unit_of_work = MagicMock()

    unit_of_work.__enter__.return_value = unit_of_work

    unit_of_work.products.get_by_ids.return_value = [
        product_1,
        product_2,
        product_3,
    ]

    service = ProductBestsellingService(
        unit_of_work=unit_of_work,
    )

    result = service.get_bestselling(
        product_ids=[3, 1, 2],
    )

    assert [product.id for product in result] == [
        3,
        1,
        2,
    ]

def test_get_bestselling_returns_empty_list():

    unit_of_work = MagicMock()

    unit_of_work.__enter__.return_value = unit_of_work
    unit_of_work.products.get_by_ids.return_value = []

    service = ProductBestsellingService(
        unit_of_work=unit_of_work,
    )

    result = service.get_bestselling(
        product_ids=[],
    )

    assert result == []

    unit_of_work.products.get_by_ids.assert_called_once_with(
        product_ids=[],
    )