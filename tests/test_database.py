from sqlalchemy import text

from app.infrastructure.database import engine


def main():

    try:

        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT version();")
            )

            version = result.scalar()

            print("Conexión exitosa")

            print()

            print(version)


    except Exception as error:

        print("Error de conexión")

        print(error)


if __name__ == "__main__":
    main()