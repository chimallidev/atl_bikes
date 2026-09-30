from pathlib import Path

from app.infrastructure.weather.timezone_location import (
    TimezoneLocation,
)


ZONE1970_PATH = Path(
    "app/infrastructure/weather/data/zone1970.tab"
)


def test_get_location_for_mexico_city():
    timezone_location = TimezoneLocation(
        ZONE1970_PATH
    )

    location = timezone_location.get_location(
        "America/Mexico_City"
    )

    assert location is not None

    assert location.latitude == 19.4
    assert location.longitude == -99.15