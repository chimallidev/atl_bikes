class FeaturedProductsLimitExceededError(Exception):
    """Se alcanzó el límite de productos destacados."""

    def __init__(self, limit: int = 3) -> None:
        super().__init__(
            f"No puede haber más de {limit} productos destacados."
        )