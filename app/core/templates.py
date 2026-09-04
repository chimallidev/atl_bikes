from pathlib import Path
from fastapi.templating import Jinja2Templates
from .template_filters import currency

BASE_DIR= Path(__file__).resolve().parent.parent

templates = Jinja2Templates(directory= BASE_DIR / "templates")

templates.env.filters["currency"] = currency