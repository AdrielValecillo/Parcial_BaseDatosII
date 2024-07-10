from pydantic import BaseModel, Field
from datetime import date, time

class TurnoBase(BaseModel):
    fecha_inicio: date = Field(..., example="2021-10-01")
    fecha_fin: date = Field(..., example="2021-10-02")
    id_servicio: int = Field(..., gt=0, example=1)

class TurnoCreate(TurnoBase):
    pass

class Turno(TurnoBase):
    id_turno: int
    id_servicio: int
    fecha_turno: date
    hora_inicio: time
    hora_fin: time
    estado: bool

    class Config:
        orm_mode = True
        from_attributes = True
