from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes.home import router as home_router

BASE_DIR = Path(__file__).resolve().parent

def create_app(root_path: str = "") -> FastAPI :
    app = FastAPI(root_path= root_path)

    #Archivos estáticos (infraestructura)
    app.mount("/static", StaticFiles(directory= BASE_DIR / "static"), name= "static")

    #Rutas
    app.include_router(home_router)

    return app