from sqlalchemy import func, select
from sqlalchemy.orm import Session

from ...domain.entities.product import Product
from ...domain.repositories.product_repository import (
    ProductRepository,
)
from ...infrastructure.mappers.product_mapper import (
    ProductMapper,
)
from ...infrastructure.models.catalog import ProductModel


class SQLAlchemyProductRepository(ProductRepository):

    def __init__(
        self,
        session: Session,
    ) -> None:
        self._session = session

    def count_featured(self) -> int:

        statement = (
            select(
                func.count(ProductModel.id)
            )
            .where(
                ProductModel.is_featured.is_(True)
            )
        )

        result = self._session.execute(statement)

        return result.scalar_one()

    def get_featured(
        self,
        limit: int,
    ) -> list[Product]:

        statement = (
            select(ProductModel)
            .where(
                ProductModel.is_featured.is_(True)
            )
            .order_by(ProductModel.id)
            .limit(limit)
        )

        result = self._session.execute(statement)

        products = result.scalars().all()

        return [
            ProductMapper.to_domain(product)
            for product in products
        ]

    def set_featured(
        self,
        product_id: int,
        is_featured: bool,
    ) -> None:

        product = self._session.get(
            ProductModel,
            product_id,
        )

        if product is None:
            raise ValueError(
                f"Producto con id {product_id} no encontrado."
            )

        product.is_featured = is_featured