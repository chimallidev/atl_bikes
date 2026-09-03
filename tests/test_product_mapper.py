from decimal import Decimal

from app.domain.entities.product import Product
from app.domain.entities.product_image import ProductImage
from app.infrastructure.mappers.product_mapper import ProductMapper
from app.infrastructure.models.catalog import (
    ProductImageModel,
    ProductModel,
)


def test_to_model_updates_product_image_models():

    product_model = ProductModel(
        id=1,
        name="Domane AL 5 Gen 4",
        slug="domane-al-5-gen-4",
        brand_id=1,
        category_id=1,
        current_price=Decimal("42999.00"),
        compare_at_price=None,
        is_featured=True,
    )

    image_model_1 = ProductImageModel(
        id=1,
        product_id=1,
        image_url="side.jpg",
        is_cover=True,
    )

    image_model_2 = ProductImageModel(
        id=2,
        product_id=1,
        image_url="front.jpg",
        is_cover=False,
    )

    product_model.images = [
        image_model_1,
        image_model_2,
    ]

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

    ProductMapper.to_model(
        product,
        product_model,
    )

    assert product_model.images[0].is_cover is False
    assert product_model.images[1].is_cover is True