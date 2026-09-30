from dataclasses import dataclass

import httpx


@dataclass(frozen=True)
class OpenWeatherResponse:
    city: str
    temperature: float
    description: str
    weather_id: int


class OpenWeatherClient:
    """
    Cliente para consultar el clima actual en OpenWeather.
    """

    BASE_URL = (
        "https://api.openweathermap.org/data/2.5/weather"
    )

    def __init__(
        self,
        api_key: str,
    ) -> None:
        self._api_key = api_key

    def get_current_weather(
        self,
        latitude: float,
        longitude: float,
    ) -> OpenWeatherResponse:

        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": self._api_key,
            "units": "metric",
            "lang": "es",
        }

        response = httpx.get(
            self.BASE_URL,
            params=params,
            timeout=10.0,
        )

        response.raise_for_status()

        data = response.json()

        return OpenWeatherResponse(
            city=data["name"],
            temperature=data["main"]["temp"],
            description=data["weather"][0]["description"],
            weather_id=data["weather"][0]["id"],
        )