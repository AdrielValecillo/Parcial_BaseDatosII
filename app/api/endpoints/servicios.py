from fastapi import APIRouter, HTTPException
from app.api.schemas import schemas_servicios as schemas
from app.services.servicios_services import ServicioServices

servicio_router = APIRouter()
crud = ServicioServices()

@servicio_router.post("/api/servicios", tags=["servicios"])
def create_servicio(servicio: schemas.ServicioBase):
    try:
        servicio = crud.create_servicio(servicio)
        return {"status": True, "data": servicio, "message": "Servicio creado correctamente", "code": 201}
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@servicio_router.get("/api/servicios", tags=["servicios"])
def get_servicios():
    try:
        servicios = crud.get_servicios()
        return {"status": True, "data": servicios, "message": "Servicios obtenidos correctamente", "code": 200}
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))
    