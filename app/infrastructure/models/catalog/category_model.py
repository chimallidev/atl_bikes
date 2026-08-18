from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from ...database.base import Base
from ....infrastructure.mixins import (
    IdMixin,
    TimestampMixin,
)


class CategoryModel(
    Base,
    IdMixin,
    TimestampMixin,
):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        comment="Nombre de la categoría.",
    )

    slug: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        comment="Slug utilizado en la URL.",
    )

    image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
        comment="Imagen representativa de la categoría.",
    )

    products = relationship(
        "ProductModel",
        back_populates="category",
    )