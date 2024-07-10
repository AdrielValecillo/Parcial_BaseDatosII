from app.services.base import Base
from app.db.models import Servicio, Comercio
from app.api.schemas.schemas_servicios import ServicioBase
from sqlalchemy.orm import joinedload

class ServicioServices(Base):

    def create_servicio(self, servicio: ServicioBase):
        db_servicio = Servicio(**servicio.dict())
        self.db.add(db_servicio)
        self.db.commit()
        self.db.refresh(db_servicio)
        return db_servicio
    
    def get_servicios(self):
        servicios = self.db.query(Servicio).options(
            joinedload(Servicio.comercio),
        ).all()
        return servicios