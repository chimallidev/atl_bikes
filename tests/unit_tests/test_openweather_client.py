from unittest.mock import Mock
from unittest.mock import patch

from app.infrastructure.weather.openweather_client import (
    OpenWeatherClient,
    OpenWeatherResponse,
)


def test_get_current_weather():

    client = OpenWeatherClient(
        api_key="test-api-key",
    )

    mock_response = Mock()

    mock_response.json.return_value = {
        "name": "Ciudad de México",
        "main": {
            "temp": 24.3,
        },
        "weather": [
            {
                "id": 803,
                "description": "nubes dispersas",
            }
        ],
    }

    with patch(
        "app.infrastructure.weather.openweather_client.httpx.get",
        return_value=mock_response,
    ) as mock_get:

        result = client.get_current_weather(
            latitude=19.4,
            longitude=-99.15,
        )

    assert result == OpenWeatherResponse(
        city="Ciudad de México",
        temperature=24.3,
        description="nubes dispersas",
        weather_id=803,
    )

    mock_get.assert_called_once_with(
        OpenWeatherClient.BASE_URL,
        params={
            "lat": 19.4,
            "lon": -99.15,
            "appid": "test-api-key",
            "units": "metric",
            "lang": "es",
        },
        timeout=10.0,
    )