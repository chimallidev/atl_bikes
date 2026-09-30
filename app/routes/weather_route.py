from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query

from ..application.schemas.weather import WeatherData
from ..application.services.weather_service import WeatherService
from ..domain.exceptions.weather_exceptions import (
    WeatherTimezoneNotFoundError,
)
from ..routes.dependencies.weather import get_weather_service


router = APIRouter(
    prefix="/api/weather",
    tags=["weather"],
)


@router.get(
    "",
    response_model=WeatherData,
)
def get_weather(
    timezone: str = Query(...),
    weather_service: WeatherService = Depends(
        get_weather_service,
    ),
) -> WeatherData:

    try:
        return weather_service.get_weather(timezone)

    except WeatherTimezoneNotFoundError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error