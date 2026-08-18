from abc import ABC, abstractmethod
from ..domain.repositories.product_repository import ProductRepository


class UnitOfWork(ABC):

    """
    Contrato para controlar una unidad de trabajo.

    Una implementación concreta será responsable de confirmar
    o revertir todos los cambios realizados durante un caso de uso.
    """

    products: ProductRepository
    
    @abstractmethod
    def __enter__(self) -> "UnitOfWork":
        raise NotImplementedError

    @abstractmethod
    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError