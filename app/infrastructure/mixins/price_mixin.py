from decimal import Decimal

from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class PriceMixin:
    """
    Información comercial relacionada con el precio.

    - current_price siempre existe.
    - compare_at_price es opcional y se utiliza para mostrar
      un precio de referencia (por ejemplo, un precio tachado).
    """

    compare_at_price: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True,
        comment="Precio de referencia para comparar con el precio actual.",
    )

    current_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
        comment="Precio actual de venta.",
    )