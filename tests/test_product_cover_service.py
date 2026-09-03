from decimal import Decimal

import pytest

from app.application.services.product_cover_service import (
    ProductCoverService,
)
from app.domain.entities.product import Product
from app.domain.entities.product_image import ProductImage


class FakeProductRepository:

    def __init__(
        self,
        product: Product | None,
    ) -> None:
        self.product = product

    def get_by_id(
        self,
        product_id: int,
    ) -> Product | None:

        if self.product is None:
            return None

        if self.product.id != product_id:
            return None

        return self.product

    def update(
        self,
        product: Product,
    ) -> None:

        self.product = product


class FakeUnitOfWork:

    def __init__(
        self,
        product: Product | None,
    ) -> None:
        self.products = FakeProductRepository(product)

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        pass

    def commit(self) -> None:
        pass


def test_set_cover_image_changes_product_cover():

    product = Product(
        id=1,
        name="Domane AL 5 Gen 4",
        slug="domane-al-5-gen-4",
        brand_id=1,
        category_id=1,
        current_price=Decimal("42999.00"),
        compare_at_price=None,
        is_featured=True,
        images=[
            ProductImage(
                id=1,
                product_id=1,
                image_url="side.jpg",
                is_cover=False,
            ),
            ProductImage(
                id=2,
                product_id=1,
                image_url="front.jpg",
                is_cover=True,
            ),
            ProductImage(
                id=3,
                product_id=1,
                image_url="back.jpg",
                is_cover=False,
            ),
        ],
    )

    unit_of_work = FakeUnitOfWork(
        product=product,
    )

    service = ProductCoverService(
        unit_of_work=unit_of_work,
    )

    service.set_cover_image(
        product_id=1,
        image_id=3,
    )

    assert product.images[0].is_cover is False
    assert product.images[1].is_cover is False
    assert product.images[2].is_cover is True


def test_set_cover_image_raises_error_when_product_not_found():

    unit_of_work = FakeUnitOfWork(
        product=None,
    )

    service = ProductCoverService(
        unit_of_work=unit_of_work,
    )

    with pytest.raises(ValueError):
        service.set_cover_image(
            product_id=99,
            image_id=1,
        )