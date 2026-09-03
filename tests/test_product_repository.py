from app.infrastructure.database.session import SessionLocal
from app.infrastructure.repositories.product_repository import ProductRepository


def main() -> None:
    session = SessionLocal()

    try:
        repository = ProductRepository(session)

        products = repository.get_all()

        print(f"Se encontraron {len(products)} productos.\n")

        for product in products:
            print(f"ID: {product.id}")
            print(f"Nombre: {product.name}")
            print(f"Slug: {product.slug}")
            print(f"Precio: ${product.current_price}")
            print("-" * 40)

    finally:
        session.close()


if __name__ == "__main__":
    main()