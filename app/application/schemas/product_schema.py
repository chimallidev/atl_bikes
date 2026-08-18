from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class FeaturedProductResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    slug: str
    current_price: Decimal
    compare_at_price: Decimal | None
    is_featured: bool