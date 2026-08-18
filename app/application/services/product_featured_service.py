from ...application.unit_of_work import UnitOfWork
from ...domain.entities.product import Product
from ...domain.exceptions.product_exceptions import (
    FeaturedProductsLimitExceededError,
)


class ProductFeaturedService:

    def __init__(
        self,
        unit_of_work: UnitOfWork,
    ) -> None:
        self._unit_of_work = unit_of_work

    def get_featured_products(self) -> list[Product]:

        with self._unit_of_work as unit_of_work:

            return unit_of_work.products.get_featured(
                limit=Product.MAX_FEATURED_PRODUCTS,
            )

    def feature_product(
        self,
        product_id: int,
    ) -> None:

        with self._unit_of_work as unit_of_work:

            featured_count = (
                unit_of_work.products.count_featured()
            )

            if (
                featured_count
                >= Product.MAX_FEATURED_PRODUCTS
            ):
                raise FeaturedProductsLimitExceededError(
                    Product.MAX_FEATURED_PRODUCTS
                )

            unit_of_work.products.set_featured(
                product_id=product_id,
                is_featured=True,
            )

            unit_of_work.commit()

    def unfeature_product(
        self,
        product_id: int,
    ) -> None:

        with self._unit_of_work as unit_of_work:

            unit_of_work.products.set_featured(
                product_id=product_id,
                is_featured=False,
            )

            unit_of_work.commit()