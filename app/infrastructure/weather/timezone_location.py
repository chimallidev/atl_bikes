from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Location:
    latitude: float
    longitude: float


class TimezoneLocation:
    """
    Resuelve una zona horaria IANA a una ubicación
    representativa utilizando zone1970.tab.
    """

    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path
        self._locations = self._load_locations()

    def get_location(self, timezone: str) -> Location | None:
        return self._locations.get(timezone)

    def _load_locations(self) -> dict[str, Location]:
        locations: dict[str, Location] = {}

        with self._file_path.open(
            mode="r",
            encoding="utf-8",
        ) as file:

            for line in file:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                parts = line.split("\t")

                if len(parts) < 3:
                    continue

                coordinates = parts[1]
                timezone = parts[2]

                latitude, longitude = self._parse_coordinates(
                    coordinates
                )

                locations[timezone] = Location(
                    latitude=latitude,
                    longitude=longitude,
                )

        return locations

    @staticmethod
    def _parse_coordinates(
        coordinates: str,
    ) -> tuple[float, float]:

        separator_index = coordinates.find(
            "+",
            1,
        )

        if separator_index == -1:
            separator_index = coordinates.find(
                "-",
                1,
            )

        latitude_text = coordinates[:separator_index]
        longitude_text = coordinates[separator_index:]

        latitude = TimezoneLocation._parse_coordinate(
            latitude_text,
            latitude=True,
        )

        longitude = TimezoneLocation._parse_coordinate(
            longitude_text,
            latitude=False,
        )

        return latitude, longitude

    @staticmethod
    def _parse_coordinate(
        value: str,
        *,
        latitude: bool,
    ) -> float:

        sign = -1 if value[0] == "-" else 1
        digits = value[1:]

        degree_digits = 2 if latitude else 3

        degrees = int(digits[:degree_digits])
        remaining = digits[degree_digits:]

        if len(remaining) == 2:
            minutes = int(remaining)

            coordinate = degrees + (
                minutes / 60
            )

        elif len(remaining) == 4:
            minutes = int(remaining[:2])
            seconds = int(remaining[2:])

            coordinate = (
                degrees
                + (minutes / 60)
                + (seconds / 3600)
            )

        else:
            raise ValueError(
                f"Formato de coordenada inválido: {value}"
            )

        return sign * coordinate