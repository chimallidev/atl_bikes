from abc import ABC, abstractmethod

from ...domain.entities.product import Product


class ProductRepository(ABC):

    @abstractmethod
    def count_featured(self) -> int:
        ...

    @abstractmethod
    def get_featured(
        self,
        limit: int,
    ) -> list[Product]:
        ...

    @abstractmethod
    def set_featured(
        self,
        product_id: int,
        is_featured: bool,
    ) -> None:
        ...

    @abstractmethod
    def update(
        self,
        product: Product,
    ) -> None:
        ...

    @abstractmethod
    def get_by_id(
        self,
        product_id: int,
    ) -> Product | None:
        ...