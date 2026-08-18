from sqlalchemy.orm import Session

from ..application.unit_of_work import UnitOfWork
from ..infrastructure.database.session import SessionLocal
from ..infrastructure.repositories.product_repository import (
    SQLAlchemyProductRepository,
)


class SQLAlchemyUnitOfWork(UnitOfWork):

    def __init__(self) -> None:
        self._session: Session | None = None

    def __enter__(self) -> "SQLAlchemyUnitOfWork":
        self._session = SessionLocal()

        self.products = SQLAlchemyProductRepository(
            self._session
        )

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> None:

        if self._session is None:
            return

        if exc_type is not None:
            self.rollback()

        self._session.close()

    def commit(self) -> None:

        if self._session is None:
            raise RuntimeError(
                "El UnitOfWork no ha sido iniciado."
            )

        self._session.commit()

    def rollback(self) -> None:

        if self._session is None:
            raise RuntimeError(
                "El UnitOfWork no ha sido iniciado."
            )

        self._session.rollback()