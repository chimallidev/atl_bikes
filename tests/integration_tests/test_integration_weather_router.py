from unittest.mock import Mock
from unittest.mock import patch

from app.core.config import settings

from app.infrastructure.weather.openweather_client import (
    OpenWeatherResponse,
)

from fastapi.testclient import TestClient

from app.application.schemas.weather import WeatherData
from app.application.services.weather_service import WeatherService
from app.main import app
from app.routes.dependencies.weather import get_weather_service


client = TestClient(app)


def test_get_weather():
    weather_service = Mock(spec=WeatherService)

    weather_service.get_weather.return_value = WeatherData(
        city="Ciudad de México",
        temperature=24.3,
        description="nubes dispersas",
        weather_type="cloudy",
    )

    app.dependency_overrides[
        get_weather_service
    ] = lambda: weather_service

    response = client.get(
        "/api/weather",
        params={
            "timezone": "America/Mexico_City",
        },
    )

    assert response.status_code == 200

    assert response.json() == {
        "city": "Ciudad de México",
        "temperature": 24.3,
        "description": "nubes dispersas",
        "weather_type": "cloudy",
    }

    weather_service.get_weather.assert_called_once_with(
        "America/Mexico_City",
    )

    app.dependency_overrides.clear()

def test_get_weather_requires_timezone():
    response = client.get(
        "/api/weather",
    )

    assert response.status_code == 422

def test_get_weather_with_unknown_timezone():
    response = client.get(
        "/api/weather",
        params={
            "timezone": "Invalid/Timezone",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "Zona horaria no encontrada: Invalid/Timezone",
    }

def test_get_weather_integration():
    mock_openweather_response = OpenWeatherResponse(
        city="Ciudad de México",
        temperature=24.3,
        description="nubes dispersas",
        weather_id=803,
    )

    with patch(
        "app.routes.dependencies.weather.OpenWeatherClient"
    ) as mock_client_class:

        mock_client = Mock()

        mock_client.get_current_weather.return_value = (
            mock_openweather_response
        )

        mock_client_class.return_value = mock_client

        response = client.get(
            "/api/weather",
            params={
                "timezone": "America/Mexico_City",
            },
        )

    assert response.status_code == 200

    assert response.json() == {
        "city": "Ciudad de México",
        "temperature": 24.3,
        "description": "nubes dispersas",
        "weather_type": "cloudy",
    }

    mock_client.get_current_weather.assert_called_once_with(
        latitude=19.4,
        longitude=-99.15,
    )

def test_get_weather_uses_openweather_api_key():
    mock_openweather_response = OpenWeatherResponse(
        city="Ciudad de México",
        temperature=24.3,
        description="nubes dispersas",
        weather_id=803,
    )

    with patch(
        "app.routes.dependencies.weather.OpenWeatherClient"
    ) as mock_client_class:

        mock_client = Mock()

        mock_client.get_current_weather.return_value = (
            mock_openweather_response
        )

        mock_client_class.return_value = mock_client

        response = client.get(
            "/api/weather",
            params={
                "timezone": "America/Mexico_City",
            },
        )

    assert response.status_code == 200

    mock_client_class.assert_called_once_with(
        api_key=settings.openweather_api_key,
    )