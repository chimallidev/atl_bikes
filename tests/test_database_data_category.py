from app.infrastructure.database.session import SessionLocal
from app.infrastructure.models.catalog import (
    BrandModel,
    CategoryModel,
)


def main() -> None:
    session = SessionLocal()

    try:
        brand = BrandModel(
            name="Specialized",
            slug="specialized",
            logo_url="https://example.com/trek.png",
        )

        session.add(brand)

        category = CategoryModel(
            name="Ruta",
            slug="ruta",
            image_url="https://example.com/montana.jpg",
        )

        session.add(category)

        session.commit()

        session.refresh(brand)
        session.refresh(category)

        print(f"Marca creada correctamente con ID: {brand.id}")
        print(f"Categoría creada correctamente con ID: {category.id}")

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()