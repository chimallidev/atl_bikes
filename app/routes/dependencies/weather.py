from pathlib import Path

from app.application.services.weather_service import (
    WeatherService,
)
from app.core.config import settings
from app.infrastructure.weather.openweather_client import (
    OpenWeatherClient,
)
from app.infrastructure.weather.timezone_location import (
    TimezoneLocation,
)


ZONE1970_PATH = (
    Path(__file__).resolve().parents[2]
    / "infrastructure"
    / "weather"
    / "data"
    / "zone1970.tab"
)


def get_weather_service() -> WeatherService:
    timezone_location = TimezoneLocation(
        file_path=ZONE1970_PATH,
    )

    openweather_client = OpenWeatherClient(
        api_key=settings.openweather_api_key,
    )

    return WeatherService(
        timezone_location=timezone_location,
        openweather_client=openweather_client,
    )