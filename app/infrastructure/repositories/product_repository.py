from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

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
        self._loaded_models: dict[int, ProductModel] = {}

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
            .options(
                selectinload(ProductModel.brand),
                selectinload(ProductModel.images)
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

    def get_by_id(
        self,
        product_id: int,
    ) -> Product | None:

        statement = (
            select(ProductModel)
            .where(
                ProductModel.id == product_id
            )
            .options(
                selectinload(ProductModel.brand),
                selectinload(ProductModel.images),
            )
        )

        result = self._session.execute(statement)

        model = result.scalar_one_or_none()

        if model is None:
            return None

        self._loaded_models[product_id] = model

        return ProductMapper.to_domain(model)

    def update(
        self,
        product: Product,
    ) -> None:

        model = self._loaded_models.get(product.id)

        if model is None:
            raise ValueError(
                f"Producto con id {product.id} "
                f"no fue cargado por el repositorio."
            )

        ProductMapper.to_model(
            product,
            model,
        )

    def get_by_ids(
    self,
    product_ids: list[int],
    ):
        if not product_ids:
            return []

        statement = (
            select(ProductModel)
            .where(ProductModel.id.in_(product_ids))
            .options(
                selectinload(ProductModel.brand),
                selectinload(ProductModel.images),
            )
        )

        models = self._session.scalars(statement).all()

        return [
            ProductMapper.to_domain(model)
            for model in models
        ]