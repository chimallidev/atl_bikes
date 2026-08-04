from enum import Enum


class ProductStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    OUT_OF_STOCK = "out_of_stock"
    DISCONTINUED = "discontinued"