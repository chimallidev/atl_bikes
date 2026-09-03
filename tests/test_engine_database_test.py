from sqlalchemy import create_engine

from app.core.config import settings


test_engine = create_engine(
    settings.database_url_test,
    echo=True,
)