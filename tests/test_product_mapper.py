from decimal import Decimal

from app.domain.entities.product import Product
from app.infrastructure.mappers.product_mapper import ProductMapper
from app.infrastructure.models.catalog import (
    BrandModel,
    ProductImageModel,
    ProductModel,
)


def test_product_mapper_to_domain():

    brand_model = BrandModel(
        id=1,
        name="Specialized",
        slug="specialized",
    )

    product_model = ProductModel(
        id=1,
        name="Rockhopper",
        slug="rockhopper",
        brand_id=1,
        category_id=1,
        current_price=Decimal("15000.00"),
        compare_at_price=Decimal("17000.00"),
        is_featured=True,
    )

    product_model.brand = brand_model

    image_model = ProductImageModel(
        id=1,
        product_id=1,
        image_url="rockhopper.jpg",
        is_cover=True,
    )

    product_model.images = [image_model]

    product = ProductMapper.to_domain(product_model)

    assert isinstance(product, Product)

    assert product.id == 1
    assert product.name == "Rockhopper"
    assert product.slug == "rockhopper"

    assert product.brand is not None
    assert product.brand.name == "Specialized"

    assert product.current_price == Decimal("15000.00")
    assert product.compare_at_price == Decimal("17000.00")
    assert product.is_featured is True

    assert product.images is not None
    assert len(product.images) == 1

    assert product.images[0].image_url == "rockhopper.jpg"
    assert product.images[0].is_cover is True

    assert product.cover_image is not None
    assert product.cover_image.image_url == "rockhopper.jpg"