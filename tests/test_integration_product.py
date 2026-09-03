from sqlalchemy.orm import Session

from app.infrastructure.models.catalog import (
    ProductImageModel,
)


def test_product_with_images(
    test_db_session: Session,
    product_with_images,
):
    product, image_1, image_2 = product_with_images

    assert product.id is not None
    assert image_1.id is not None
    assert image_2.id is not None

    assert image_1.product_id == product.id
    assert image_2.product_id == product.id

    assert image_1.is_cover is True
    assert image_2.is_cover is False