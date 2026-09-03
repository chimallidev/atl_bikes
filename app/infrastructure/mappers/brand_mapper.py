from ...domain.entities.brand import Brand
from ...infrastructure.models.catalog import BrandModel


class BrandMapper:

    @staticmethod
    def to_domain(
        model: BrandModel,
    ) -> Brand:

        return Brand(
            id=model.id,
            name=model.name,
            slug=model.slug,
            logo_url=model.logo_url,
        )