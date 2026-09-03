from sqlalchemy import text
from sqlalchemy.orm import Session


def test_test_database_connection(test_db_session: Session):
    result = test_db_session.execute(text("SELECT 1"))

    assert result.scalar() == 1