from ...domain.entities.product import Product
from ...infrastructure.models.catalog import ProductModel
from ...infrastructure.mappers.brand_mapper import BrandMapper
from ...infrastructure.mappers.product_image_mapper import ProductImageMapper


class ProductMapper:

    @staticmethod
    def to_domain(model: ProductModel) -> Product:

        return Product(
            id=model.id,
            name=model.name,
            slug=model.slug,
            brand_id=model.brand_id,
            category_id=model.category_id,
            current_price=model.current_price,
            compare_at_price=model.compare_at_price,
            is_featured=model.is_featured,
            brand=(
                BrandMapper.to_domain(model.brand)
                if model.brand is not None
                else None
            ),
            images=[
                ProductImageMapper.to_domain(image)
                for image in model.images
            ]
        )

    @staticmethod
    def to_model(
        entity: Product,
        model: ProductModel,
    ) -> ProductModel:

        model.name = entity.name
        model.slug = entity.slug
        model.brand_id = entity.brand_id
        model.category_id = entity.category_id
        model.current_price = entity.current_price
        model.compare_at_price = entity.compare_at_price
        model.is_featured = entity.is_featured

        for image in entity.images or []:

            image_model = next(
                (
                    image_model
                    for image_model in model.images
                    if image_model.id == image.id
                ),
                None,
            )

            if image_model is not None:
                ProductImageMapper.to_model(
                    image,
                    image_model,
                )

        return model

    