from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from ....database.base import Base
from ....infrastructure.mixins import (
    IdMixin,
    PriceMixin,
    TimestampMixin,
)


class ProductModel(
    Base,
    IdMixin,
    PriceMixin,
    TimestampMixin,
):
    __tablename__ = "products"

    __table_args__ = (
        Index("ix_products_name", "name"),
        Index("ix_products_brand_id", "brand_id"),
        Index("ix_products_category_id", "category_id"),
        CheckConstraint(
            "current_price > 0",
            name="current_price_positive",
        ),
        CheckConstraint(
            "compare_at_price IS NULL OR compare_at_price > current_price",
            name="compare_at_price",
        ),
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        comment="Nombre comercial del producto.",
    )

    slug: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        comment="Slug utilizado en la URL.",
    )

    brand_id: Mapped[int] = mapped_column(
        ForeignKey("brands.id"),
        nullable=False,
        comment="Marca del producto.",
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False,
        comment="Categoría del producto.",
    )

    brand = relationship(
        "BrandModel",
        back_populates="products",
    )

    category = relationship(
        "CategoryModel",
        back_populates="products",
    )