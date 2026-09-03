from app.infrastructure.models.catalog import BrandModel


def main() -> None:
    print("Modelo:", BrandModel)
    print("Tabla:", BrandModel.__tablename__)


if __name__ == "__main__":
    main()