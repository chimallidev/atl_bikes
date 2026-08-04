from sqlalchemy import select
from sqlalchemy.orm import Session

from ...infrastructure.models.catalog import ProductModel


class ProductRepository:

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_all(self) -> list[ProductModel]:

        result = self._session.execute(
            select(ProductModel)
        )

        return result.scalars().all()