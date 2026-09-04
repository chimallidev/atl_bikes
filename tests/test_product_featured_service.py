from decimal import Decimal

from app.application.schemas.product_schema import FeaturedProductResponse
from app.application.services.product_featured_service import (
    ProductFeaturedService,
)
from app.domain.entities.brand import Brand
from app.domain.entities.product import Product
from app.domain.entities.product_image import ProductImage


class FakeProductRepository:

    def __init__(self, products):
        self.products = products

    def get_featured(self, limit: int):
        return self.products[:limit]


class FakeUnitOfWork:

    def __init__(self, products):
        self.products = FakeProductRepository(products)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


def test_get_featured_returns_expected_product_data():

    brand = Brand(
        id=1,
        name="Specialized",
        slug="specialized",
    )

    product = Product(
        id=1,
        name="Rockhopper",
        slug="rockhopper",
        brand_id=1,
        category_id=1,
        current_price=Decimal("15000.00"),
        compare_at_price=Decimal("17000.00"),
        is_featured=True,
        brand=brand,
        images=[
            ProductImage(
                id=1,
                product_id=1,
                image_url="rockhopper.jpg",
                is_cover=True,
            )
        ],
    )

    unit_of_work = FakeUnitOfWork([product])

    assert product.brand is not None
    assert product.brand.name == "Specialized"

    assert product.cover_image is not None
    assert product.cover_image.image_url == "rockhopper.jpg"

    service = ProductFeaturedService(unit_of_work)

    response = service.get_featured()

    assert len(response) == 1

    assert response[0].id == 1
    assert response[0].name == "Rockhopper"
    assert response[0].slug == "rockhopper"
    assert response[0].brand == "Specialized"
    assert response[0].current_price == Decimal("15000.00")
    assert response[0].compare_at_price == Decimal("17000.00")
    assert response[0].is_featured is True
    assert response[0].cover_image_url == "rockhopper.jpg"