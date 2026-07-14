import uuid

from datetime import UTC ,datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .....core.database import Base



class CategoryModel(Base):

    __tablename__ = "categories"


    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )


    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )


    slug: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False
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


    products = relationship(
        "ProductModel",
        back_populates="category"
    )