from unittest.mock import Mock

from app.application.schemas.weather import WeatherData
from app.application.services.weather_service import (
    WeatherService,
)
from app.infrastructure.weather.openweather_client import (
    OpenWeatherResponse,
)
from app.infrastructure.weather.timezone_location import (
    Location,
)

from app.domain.exceptions.weather_exceptions import (
    WeatherTimezoneNotFoundError,
)


def test_get_weather():

    timezone_location = Mock()

    timezone_location.get_location.return_value = Location(
        latitude=19.4,
        longitude=-99.15,
    )

    openweather_client = Mock()

    openweather_client.get_current_weather.return_value = (
        OpenWeatherResponse(
            city="Ciudad de México",
            temperature=24.3,
            description="nubes dispersas",
            weather_id=803,
        )
    )

    service = WeatherService(
        timezone_location=timezone_location,
        openweather_client=openweather_client,
    )

    result = service.get_weather(
        "America/Mexico_City"
    )

    assert result == WeatherData(
        city="Ciudad de México",
        temperature=24.3,
        description="nubes dispersas",
        weather_type="cloudy",
    )

    timezone_location.get_location.assert_called_once_with(
        "America/Mexico_City"
    )

    openweather_client.get_current_weather.assert_called_once_with(
        latitude=19.4,
        longitude=-99.15,
    )

def test_get_weather_raises_error_for_unknown_timezone():

    timezone_location = Mock()

    timezone_location.get_location.return_value = None

    openweather_client = Mock()

    service = WeatherService(
        timezone_location=timezone_location,
        openweather_client=openweather_client,
    )

    try:
        service.get_weather("Invalid/Timezone")
    except WeatherTimezoneNotFoundError as error:
        assert str(error) == (
            "Zona horaria no encontrada: Invalid/Timezone"
        )
    else:
        raise AssertionError(
            "Se esperaba un WeatherTimezoneNotFoundError"
        )

    openweather_client.get_current_weather.assert_not_called()