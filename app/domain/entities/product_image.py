from dataclasses import dataclass

@dataclass
class ProductImage:
    id: int | None
    product_id: int
    image_url: str
    is_cover: bool