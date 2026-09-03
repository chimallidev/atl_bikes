from decimal import Decimal

from app.application.services.product_featured_service import ProductFeaturedService
from app.domain.entities.brand import Brand
from app.domain.entities.product import Product
from app.domain.entities.product_image import ProductImage


class FakeProductRepository:

    def __init__(
        self,
        products: list[Product],
    ) -> None:
        self.products = products
        self.received_limit = None

    def get_featured(
        self,
        limit: int,
    ) -> list[Product]:

        self.received_limit = limit

        return self.products[:limit]


class FakeUnitOfWork:

    def __init__(
        self,
        products: list[Product],
    ) -> None:
        self.products = FakeProductRepository(products)

    def __enter__(self) -> "FakeUnitOfWork":
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> None:
        pass


def test_get_featured_returns_brand_and_cover_image():

    product = Product(
        id=1,
        name="Domane AL 5 Gen 4",
        slug="domane-al-5-gen-4",
        brand_id=1,
        category_id=1,
        current_price=Decimal("42999.00"),
        compare_at_price=None,
        is_featured=True,
        brand=Brand(
            id=1,
            name="Trek",
            slug="trek",
        ),
        images=[
            ProductImage(
                id=1,
                product_id=1,
                image_url="https://example.com/domane-side.jpg",
                is_cover=False,
            ),
            ProductImage(
                id=2,
                product_id=1,
                image_url="https://example.com/domane-cover.jpg",
                is_cover=True,
            ),
        ],
    )

    unit_of_work = FakeUnitOfWork(
        products=[product],
    )

    service = ProductFeaturedService(
        unit_of_work=unit_of_work,
    )

    response = service.get_featured()

    assert len(response) == 1

    assert response[0].name == "Domane AL 5 Gen 4"

    assert response[0].brand == "Trek"

    assert response[0].current_price == Decimal(
        "42999.00"
    )

    assert response[0].is_featured is True

    assert response[0].cover_image_url == (
        "https://example.com/domane-cover.jpg"
    )

def test_get_featured_uses_max_featured_products_limit():

    product = Product(
        id=1,
        name="Domane AL 5 Gen 4",
        slug="domane-al-5-gen-4",
        brand_id=1,
        category_id=1,
        current_price=Decimal("42999.00"),
        compare_at_price=None,
        is_featured=True,
        brand=Brand(
            id=1,
            name="Trek",
            slug="trek",
        ),
        images=[
            ProductImage(
                id=1,
                product_id=1,
                image_url="https://example.com/domane-cover.jpg",
                is_cover=True,
            ),
        ],
    )

    unit_of_work = FakeUnitOfWork(
        products=[product],
    )

    service = ProductFeaturedService(
        unit_of_work=unit_of_work,
    )

    service.get_featured()

    assert (
        unit_of_work.products.received_limit
        == Product.MAX_FEATURED_PRODUCTS
    )