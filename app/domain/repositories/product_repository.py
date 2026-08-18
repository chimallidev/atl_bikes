from abc import ABC, abstractmethod

from ...domain.entities.product import Product


class ProductRepository(ABC):

    @abstractmethod
    def count_featured(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_featured(
        self,
        limit: int,
    ) -> list[Product]:
        raise NotImplementedError

    @abstractmethod
    def set_featured(
        self,
        product_id: int,
        is_featured: bool,
    ) -> None:
        raise NotImplementedError