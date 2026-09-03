from ...domain.repositories.product_repository import ProductRepository
from ...application.unit_of_work import UnitOfWork


class ProductCoverService:

    def __init__(
        self,
        unit_of_work: UnitOfWork,
    ) -> None:
        self._unit_of_work = unit_of_work

    def set_cover_image(
        self,
        product_id: int,
        image_id: int,
    ) -> None:

        with self._unit_of_work as uow:

            product = uow.products.get_by_id(
                product_id
            )

            if product is None:
                raise ValueError(
                    f"Producto con id {product_id} "
                    f"no encontrado."
                )

            product.set_cover_image(
                image_id
            )

            uow.products.update(
                product
            )

            self._unit_of_work.commit()