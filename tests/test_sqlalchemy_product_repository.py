from decimal import Decimal

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.domain.entities.product import Product
from app.infrastructure.database.base import Base
from app.infrastructure.models.catalog import (
    ProductImageModel,
    ProductModel,
)
from app.infrastructure.repositories.product_repository import (
    SQLAlchemyProductRepository,
)


def test_update_product_updates_product_model():

    engine = create_engine(
        "sqlite:///:memory:",
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:

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

        session.add(product_model)
        session.commit()

        repository = SQLAlchemyProductRepository(
            session,
        )

        product = repository.get_by_id(1)

        print(
            "loaded model:",
            repository._loaded_models[1],
        )

        print(
            "original model:",
            product_model,
        )

        print(
            "same object:",
            repository._loaded_models[1] is product_model,
        )

        assert product is not None

        product.is_featured = False

        repository.update(product)

        print(
            "product.is_featured:",
            product.is_featured,
        )

        print(
            "product_model.is_featured:",
            product_model.is_featured,
        )

        session.flush()

        assert product_model.is_featured is False

def test_update_product_updates_cover_image():

    engine = create_engine(
        "sqlite:///:memory:",
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:

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

        image_1 = ProductImageModel(
            id=1,
            product_id=1,
            image_url="https://example.com/domane-side.jpg",
            is_cover=True,
        )

        image_2 = ProductImageModel(
            id=2,
            product_id=1,
            image_url="https://example.com/domane-front.jpg",
            is_cover=False,
        )

        product_model.images = [
            image_1,
            image_2,
        ]

        session.add(product_model)
        session.commit()

        repository = SQLAlchemyProductRepository(
            session,
        )

        product = repository.get_by_id(1)

        assert product is not None

        product.set_cover_image(2)

        repository.update(product)

        session.flush()

        assert image_1.is_cover is False
        assert image_2.is_cover is True