from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ....infrastructure.database.base import Base
from ....infrastructure.mixins.id_mixin import IdMixin
from ....infrastructure.mixins.timestamp_mixin import TimestampMixin


class ProductImageModel(
    IdMixin,
    TimestampMixin,
    Base,
):
    __tablename__ = "product_images"

    product_id: Mapped[int] = mapped_column(
        ForeignKey(
            "products.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    image_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    is_cover: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    product: Mapped["ProductModel"] = relationship(
        "ProductModel",
        back_populates="images",
    )