import uuid

from datetime import UTC ,datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.core.database import Base



class ProductModel(Base):

    __tablename__ = "products"


    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )


    brand_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("brands.id"),
        nullable=False
    )


    category_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )


    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )


    slug: Mapped[str] = mapped_column(
        String(180),
        unique=True,
        nullable=False
    )


    previous_price: Mapped[float | None] = mapped_column(
        Numeric(10,2),
        nullable=True
    )


    current_price: Mapped[float] = mapped_column(
        Numeric(10,2),
        nullable=False
    )


    is_featured: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )


    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC)
    )


    brand = relationship(
        "BrandModel",
        back_populates="products"
    )


    category = relationship(
        "CategoryModel",
        back_populates="products"
    )