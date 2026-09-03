from decimal import Decimal

import pytest

from app.domain.entities.product import Product
from app.domain.entities.product_image import ProductImage


def test_set_cover_image_replaces_previous_cover():

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

    product.set_cover_image(3)

    assert product.images[0].is_cover is False
    assert product.images[1].is_cover is False
    assert product.images[2].is_cover is True

def test_set_cover_image_raises_error_for_invalid_image():

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
        ],
    )

    with pytest.raises(ValueError):
        product.set_cover_image(99)

def test_set_cover_image_keeps_previous_cover_when_image_not_found():

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
        ],
    )

    with pytest.raises(ValueError):
        product.set_cover_image(99)

    assert product.images[0].is_cover is False
    assert product.images[1].is_cover is True

def test_set_cover_image_raises_error_when_product_has_no_images():

    product = Product(
        id=1,
        name="Domane AL 5 Gen 4",
        slug="domane-al-5-gen-4",
        brand_id=1,
        category_id=1,
        current_price=Decimal("42999.00"),
        compare_at_price=None,
        is_featured=True,
        images=[],
    )

    with pytest.raises(ValueError):
        product.set_cover_image(1)

def test_validate_cover_image_requires_a_cover():

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
                is_cover=False,
            ),
        ],
    )

    with pytest.raises(ValueError):
        product.validate_cover_image()

def test_validate_cover_image_accepts_one_cover():

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
        ],
    )

    product.validate_cover_image()

def test_validate_cover_image_rejects_multiple_covers():

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
                is_cover=True,
            ),
            ProductImage(
                id=2,
                product_id=1,
                image_url="front.jpg",
                is_cover=True,
            ),
        ],
    )

    with pytest.raises(ValueError):
        product.validate_cover_image()