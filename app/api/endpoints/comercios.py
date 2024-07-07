from fastapi import APIRouter, HTTPException
from app.api.schemas import schemas_comercios as schemas
from app.services.comercios_services import ComercioServices

comercio_router = APIRouter()
crud = ComercioServices()

@comercio_router.post("/api/comercios", tags=["comercios"])
def create_comercio(comercio: schemas.ComercioBase):
    try:
        comercio = crud.create_comercio(comercio)
        return {"status": True, "data": comercio, "message": "Comercio creado correctamente", "code": 201}
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))



@comercio_router.get("/api/comercios", tags=["comercios"])
def get_comercios():
    try:
        comercios = crud.get_comercios()
        return {"status": True, "data": comercios, "message": "Comercios obtenidos correctamente", "code": 200}
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))
    