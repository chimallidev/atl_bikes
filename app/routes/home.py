from pathlib import Path

from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import HTMLResponse

from ..application.services.product_featured_service import (
    ProductFeaturedService,
)
from ..infrastructure.unit_of_work import (
    SQLAlchemyUnitOfWork,
)
from ..core.templates import templates


router = APIRouter()


@router.get(
    "/",
    name="atl_home",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
)
async def home(request: Request):

    template_path = Path(
        templates.env.loader.searchpath[0]
    ) / "index.html"

    if not template_path.is_file():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La página ATL Bikes no ha sido encontrada.",
        )

    try:
        unit_of_work = SQLAlchemyUnitOfWork()

        service = ProductFeaturedService(
            unit_of_work=unit_of_work,
        )

        featured_products = service.get_featured()

    except Exception as error:

        print(
        f"ERROR EN HOME: {type(error).__name__}: {error}"
        )
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No fue posible obtener los productos destacados.",
        ) from error

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "featured_products": featured_products,
        },
    )