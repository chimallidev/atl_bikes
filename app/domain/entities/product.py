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

    MAX_FEATURED_PRODUCTS = 3