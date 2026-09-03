from app.infrastructure.models.catalog import CategoryModel


def main() -> None:
    print("Modelo:", CategoryModel)
    print("Tabla:", CategoryModel.__tablename__)


if __name__ == "__main__":
    main()