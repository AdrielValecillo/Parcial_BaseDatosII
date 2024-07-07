from pydantic import BaseModel, constr, conint

class ComercioBase(BaseModel):
    nom_comercio: constr(min_length=1, max_length=100)
    aforo_maximo: conint(gt=0)

class ComercioCreate(ComercioBase):
    pass

class Comercio(ComercioBase):
    id_comercio: int

    class Config:
        from_attributes = True
        orm_mode = True