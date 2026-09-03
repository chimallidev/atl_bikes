from sqlalchemy import select

from app.infrastructure.database.session import SessionLocal

from app.infrastructure.models.catalog import (
    BrandModel,
    CategoryModel,
    ProductModel,
)


def main() -> None:
    session = SessionLocal()

    try:
        # Buscar la marca
        result = session.execute(
            select(BrandModel).where(
                BrandModel.name == "Trek"
            )
        )

        brand = result.scalar_one_or_none()

        if brand is None:
            raise ValueError("No existe la marca 'Trek'.")

        # Buscar la categoría
        result = session.execute(
            select(CategoryModel).where(
                CategoryModel.name == "Ruta"
            )
        )

        category = result.scalar_one_or_none()

        if category is None:
            raise ValueError("No existe la categoría 'Ruta'.")

        # Crear el producto
        product = ProductModel(
            name="Domane AL 5 Gen 4",
            slug="domane-al-5-gen-4",
            brand_id=brand.id,
            category_id=category.id,
            current_price=42999.00,
            compare_at_price=46999.00,
        )

        session.add(product)

        session.commit()

        session.refresh(product)

        print(f"Producto creado correctamente con ID: {product.id}")

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()