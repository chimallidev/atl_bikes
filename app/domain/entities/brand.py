from dataclasses import dataclass


@dataclass
class Brand:
    id: int
    name: str
    slug: str
    logo_url: str | None = None