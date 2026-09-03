from sqlalchemy import text


def test_database_session(db_session):
    result = db_session.execute(text("SELECT 1"))

    print("result=", result)

    assert result.scalar() == 1