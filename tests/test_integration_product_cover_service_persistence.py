from sqlalchemy.orm import Session

from app.application.services.product_cover_service import (
    ProductCoverService,
)
from app.infrastructure.models.catalog import (
    ProductImageModel,
)
from app.infrastructure.unit_of_work import (
    SQLAlchemyUnitOfWork,
)
from tests.test_engine_database_test import test_engine


def test_set_cover_image(
    use_test_database,
    product_with_images,
):
    product, image_1, image_2 = product_with_images

    service = ProductCoverService(
        SQLAlchemyUnitOfWork()
    )

    service.set_cover_image(
        product_id=product.id,
        image_id=image_2.id,
    )

    with Session(test_engine) as session:

        image_1_db = session.get(
            ProductImageModel,
            image_1.id,
        )

        image_2_db = session.get(
            ProductImageModel,
            image_2.id,
        )

    assert image_1_db is not None
    assert image_2_db is not None

    assert image_1_db.is_cover is False
    assert image_2_db.is_cover is True