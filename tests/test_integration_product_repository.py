from sqlalchemy import select, text

from app.domain.entities.product import Product

from app.infrastructure.models.catalog import ProductModel

from app.infrastructure.repositories.product_repository import SQLAlchemyProductRepository


def test_database_contains_featured_products(db_session):

    statement = (
        select(ProductModel)
        .where(
            ProductModel.is_featured.is_(True)
        )
    )

    result = db_session.execute(statement)

    products = result.scalars().all()

    print(f"\nProductos featured encontrados: {len(products)}")

    for product in products:
        print(
            f"id={product.id}, "
            f"name={product.name}, "
            f"is_featured={product.is_featured}"
        )

    assert len(products) > 0

def test_database_contains_products(test_db_session):

    statement = select(ProductModel)

    result = test_db_session.execute(statement)

    products = result.scalars().all()

    print(f"\nProductos encontrados: {len(products)}")

    for product in products:
        print(
            f"id={product.id}, "
            f"name={product.name}, "
            f"is_featured={product.is_featured}"
        )

    assert len(products) > 0

def test_database_connection(test_db_session):

    result = test_db_session.execute(
        text("SELECT current_database()")
    )

    database = result.scalar_one()

    print(
        f"\nBase de datos utilizada por el test: {database}"
    )

    assert database == "atl_bikes_test"

def test_product_fixture(test_db_session, product_with_images):

    product, image_1, image_2 = product_with_images

    products = test_db_session.execute(
        select(ProductModel)
    ).scalars().all()

    print(f"\nProductos encontrados: {len(products)}")

    for item in products:
        print(
            f"id={item.id}, "
            f"name={item.name}, "
            f"is_featured={item.is_featured}"
        )

    assert len(products) == 1
    assert products[0].id == product.id

def test_get_featured_returns_products(
    test_db_session,
    product_with_images,
):

    product, image_1, image_2 = product_with_images

    product.is_featured = True
    test_db_session.commit()

    repository = SQLAlchemyProductRepository(
        test_db_session
    )

    products = repository.get_featured(
        limit=Product.MAX_FEATURED_PRODUCTS
    )

    print(f"\nFeatured encontrados: {len(products)}")

    for item in products:
        print(
            f"id={item.id}, "
            f"name={item.name}, "
            f"is_featured={item.is_featured}"
        )

    assert len(products) == 1

    assert products[0].id == product.id
    assert products[0].name == "Test Bike"
    assert products[0].is_featured is True

