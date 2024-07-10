from pydantic import BaseModel, constr, conint
from datetime import date, time

class ServicioBase(BaseModel):
    nom_servicio: constr(min_length=1, max_length=100)
    id_comercio: conint(gt=0)
    hora_apertura: time
    hora_cierre: time
    duracion: int



class ServicioCreate(ServicioBase):
    pass

class Servicio(ServicioBase):
    id_servicio: int

    class Config:
        from_attributes = True
        orm_mode = True
