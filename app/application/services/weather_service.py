from app.application.schemas.weather import WeatherData
from app.infrastructure.weather.openweather_client import (
    OpenWeatherClient,
)
from app.infrastructure.weather.timezone_location import (
    TimezoneLocation,
)

from app.domain.exceptions.weather_exceptions import (
    WeatherTimezoneNotFoundError,
)


class WeatherService:

    def __init__(
        self,
        timezone_location: TimezoneLocation,
        openweather_client: OpenWeatherClient,
    ) -> None:
        self._timezone_location = timezone_location
        self._openweather_client = openweather_client

    def get_weather(
        self,
        timezone: str,
    ) -> WeatherData:

        location = self._timezone_location.get_location(
            timezone
        )

        if location is None:
            raise WeatherTimezoneNotFoundError(
                timezone
            )

        weather = self._openweather_client.get_current_weather(
            latitude=location.latitude,
            longitude=location.longitude,
        )

        weather_type = self._get_weather_type(
            weather.weather_id
        )

        return WeatherData(
            city=weather.city,
            temperature=weather.temperature,
            description=weather.description,
            weather_type=weather_type,
        )

    @staticmethod
    def _get_weather_type(
        weather_id: int,
    ) -> str:

        if weather_id == 800:
            return "clear"

        if 801 <= weather_id <= 802:
            return "partly_cloudy"

        if 803 <= weather_id <= 804:
            return "cloudy"

        if 200 <= weather_id <= 232:
            return "storm"

        if 300 <= weather_id <= 321:
            return "rain"

        if 500 <= weather_id <= 531:
            return "rain"

        if 600 <= weather_id <= 622:
            return "snow"

        if 701 <= weather_id <= 781:
            return "fog"

        return "cloudy"