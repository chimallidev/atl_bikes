from ...domain.entities.brand import Brand
from ...domain.entities.product_image import ProductImage
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    id: int
    name: str
    slug: str
    brand_id: int
    category_id: int
    current_price: Decimal
    compare_at_price: Decimal | None
    is_featured: bool
    brand: Brand | None = None
    images: list[ProductImage] | None = None

    MAX_FEATURED_PRODUCTS = 3

    @property
    def cover_image(self) -> ProductImage | None:
        if not self.images:
            return None

        return next(
            (
                image
                for image in self.images
                if image.is_cover
            ),
            None,
        )

    def set_cover_image(self, image_id: int) -> None:

        if not self.images:
            raise ValueError(
                "El producto no tiene imágenes."
            )

        image_to_cover = next(
            (
                image
                for image in self.images
                if image.id == image_id
            ),
            None,
        )

        if image_to_cover is None:
            raise ValueError(
                f"La imagen con id {image_id} "
                f"no pertenece al producto."
            )

        for image in self.images:
            image.is_cover = image is image_to_cover

    def validate_cover_image(self) -> None:

        if not self.images:
            raise ValueError(
                "El producto debe tener al menos una imagen."
            )

        cover_count = sum(
            image.is_cover
            for image in self.images
        )

        if cover_count == 0:
            raise ValueError(
                "El producto debe tener una imagen de portada."
            )

        if cover_count > 1:
            raise ValueError(
                "El producto no puede tener más de una imagen de portada."
            )
