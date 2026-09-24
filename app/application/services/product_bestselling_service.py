from ...application.unit_of_work import UnitOfWork
from ...application.schemas.product_schema import (
    BestsellingProductResponse,
)


class ProductBestsellingService:

    def __init__(
        self,
        unit_of_work: UnitOfWork,
    ) -> None:
        self._unit_of_work = unit_of_work

    def get_bestselling(
        self,
        product_ids: list[int],
    ) -> list[BestsellingProductResponse]:

        with self._unit_of_work as uow:

            products = uow.products.get_by_ids(
                product_ids=product_ids,
            )

        products_by_id = {
            product.id: product
            for product in products
        }

        return [
            BestsellingProductResponse(
                id=products_by_id[product_id].id,
                name=products_by_id[product_id].name,
                slug=products_by_id[product_id].slug,
                brand=products_by_id[product_id].brand.name,
                current_price=products_by_id[
                    product_id
                ].current_price,
                compare_at_price=products_by_id[
                    product_id
                ].compare_at_price,
                is_featured=products_by_id[
                    product_id
                ].is_featured,
                cover_image_url=products_by_id[
                    product_id
                ].cover_image.image_url,
            )
            for product_id in product_ids
            if product_id in products_by_id
        ]