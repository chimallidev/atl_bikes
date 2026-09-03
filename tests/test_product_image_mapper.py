from app.domain.entities.product_image import ProductImage
from app.infrastructure.mappers.product_image_mapper import (
    ProductImageMapper,
)
from app.infrastructure.models.catalog import ProductImageModel


def test_product_image_mapper_to_domain():

    model = ProductImageModel(
        id=1,
        product_id=10,
        image_url="https://example.com/image.jpg",
        is_cover=True,
    )

    entity = ProductImageMapper.to_domain(model)

    assert isinstance(entity, ProductImage)
    assert entity.id == 1
    assert entity.product_id == 10
    assert entity.image_url == "https://example.com/image.jpg"
    assert entity.is_cover is True