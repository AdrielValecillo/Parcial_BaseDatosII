import json
from fastapi import APIRouter, HTTPException
from app.api.schemas import schemas_turnos as schemas
from app.services.turnos_services import TurnoServices
from typing import List

turno_router = APIRouter()
crud = TurnoServices()

@turno_router.post("/api/turnos", tags=["turnos"])
def generate_turno(turno: schemas.TurnoBase):
    try:
        turnos_generados = crud.generate_turno(turno)
        for turno in turnos_generados:
            print(turno.id_turno, turno.id_servicio, turno.hora_inicio, turno.hora_fin, turno.fecha_turno, turno.estado)

        return {"status": True, "data": turnos_generados, "message": "Turno creado correctamente", "code": 201}
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@turno_router.get("/api/turnos/{nom_comercio}", tags=["turnos"])
def get_last_turno(nom_comercio: str):
    try:
        turno = crud.get_last_turno(nom_comercio)
        return {"status": True, "data": turno, "message": "Turno obtenido correctamente", "code": 200}
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))
    