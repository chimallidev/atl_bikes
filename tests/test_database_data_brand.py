from app.infrastructure.database.session import SessionLocal
from app.infrastructure.models.catalog import BrandModel


def main() -> None:
    session = SessionLocal()

    try:
        brand = BrandModel(
            name="Trek",
            slug="trek",
            logo_url="https://example.com/trek.png",
        )

        session.add(brand)

        session.commit()

        session.refresh(brand)

        print(f"Marca creada correctamente con ID: {brand.id}")

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()