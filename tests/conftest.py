import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.infrastructure.database.base import Base
from app.infrastructure.database import session as database_session
from tests.test_engine_database_test import test_engine

from decimal import Decimal

from app.infrastructure.models.catalog import (
    BrandModel,
    CategoryModel,
    ProductImageModel,
    ProductModel,
)



@pytest.fixture
def db_session() -> Session:
    engine = create_engine(
        "sqlite:///:memory:",
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    Base.metadata.drop_all(engine)


@pytest.fixture
def test_db_session() -> Session:
    TestingSessionLocal = sessionmaker(
        bind=test_engine,
        autoflush=False,
        autocommit=False,
    )

    with TestingSessionLocal() as session:
        yield session


@pytest.fixture
def use_test_database(monkeypatch, test_db_session):
    monkeypatch.setattr(
        database_session,
        "SessionLocal",
        lambda: test_db_session,
    )

@pytest.fixture
def product_with_images(test_db_session):

    brand = BrandModel(
        name="Test Brand",
        slug="test-brand",
    )

    category = CategoryModel(
        name="Test Category",
        slug="test-category",
    )

    product = ProductModel(
        name="Test Bike",
        slug="test-bike",
        brand=brand,
        category=category,
        current_price=Decimal("1000.00"),
        is_featured=False,
    )

    image_1 = ProductImageModel(
        product=product,
        image_url="https://test.com/image-1.jpg",
        is_cover=True,
    )

    image_2 = ProductImageModel(
        product=product,
        image_url="https://test.com/image-2.jpg",
        is_cover=False,
    )

    test_db_session.add(product)
    test_db_session.commit()

    test_db_session.refresh(product)
    test_db_session.refresh(image_1)
    test_db_session.refresh(image_2)

    yield product, image_1, image_2

    test_db_session.delete(product)
    test_db_session.delete(category)
    test_db_session.delete(brand)

    test_db_session.commit()

@pytest.fixture
def use_test_database(monkeypatch):

    TestingSessionLocal = sessionmaker(
        bind=test_engine,
        autoflush=False,
        autocommit=False,
    )

    monkeypatch.setattr(
        "app.infrastructure.unit_of_work.SessionLocal",
        TestingSessionLocal,
    )