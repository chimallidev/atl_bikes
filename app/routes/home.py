from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from ..core.templates import templates

router = APIRouter()

@router.get("/", name= "atl_home", response_class= HTMLResponse, status_code= status.HTTP_200_OK)
async def home(request: Request):
    try:
        return templates.TemplateResponse(request= request, name= "index.html", context= {})
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "La página atl bikes no ha sido encontrada.")