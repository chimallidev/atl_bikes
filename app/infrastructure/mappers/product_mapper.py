from ...domain.entities.product import Product
from ...infrastructure.models.catalog import ProductModel


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
        )