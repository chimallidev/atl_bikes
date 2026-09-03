from ...domain.entities.product_image import ProductImage
from ...infrastructure.models.catalog import ProductImageModel


class ProductImageMapper:

    @staticmethod
    def to_domain(model: ProductImageModel) -> ProductImage:

        return ProductImage(
            id=model.id,
            product_id=model.product_id,
            image_url=model.image_url,
            is_cover=model.is_cover,
        )

    @staticmethod
    def to_model(
        entity: ProductImage,
        model: ProductImageModel,
    ) -> ProductImageModel:

        model.product_id = entity.product_id
        model.image_url = entity.image_url
        model.is_cover = entity.is_cover

        return model