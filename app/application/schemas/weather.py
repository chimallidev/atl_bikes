from typing import Literal

from pydantic import BaseModel


WeatherType = Literal[
    "clear",
    "partly_cloudy",
    "cloudy",
    "rain",
    "storm",
    "snow",
    "fog",
]


class WeatherData(BaseModel):
    city: str
    temperature: float
    description: str
    weather_type: WeatherType