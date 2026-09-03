from app.core.config import settings


def main() -> None:

    print("=" * 60)

    print("Configuración del proyecto")

    print("=" * 60)

    print()

    print(f"APP_NAME: {settings.app_name}")

    print()

    print(f"DATABASE_URL: {settings.database_url}")

    print()

    print(f"DATABASE_URL_TEST: {settings.database_url_test}")
    
    print()

    print(f"SUPABASE_URL: {settings.supabase_url}")

    print()

    print(
        f"SUPABASE_PUBLISHABLE_KEY: "
        f"{settings.supabase_publishable_key[:25]}..."
    )

    print()

    print(f"SUPABASE_BUCKET: {settings.supabase_bucket}")

    print()

    print(f"ENVIRONMENT: {settings.environment}")

    print()

    print(f"TIMEZONE: {settings.timezone}")


if __name__ == "__main__":
    main()