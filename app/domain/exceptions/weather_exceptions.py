class WeatherTimezoneNotFoundError(Exception):
    """La zona horaria no tiene una ubicación asociada."""

    def __init__(self, timezone: str) -> None:
        super().__init__(
            f"Zona horaria no encontrada: {timezone}"
        )