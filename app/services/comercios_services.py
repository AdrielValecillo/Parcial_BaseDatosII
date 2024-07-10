from app.services.base import Base
from app.db.models import Comercio
from app.api.schemas.schemas_comercios import ComercioBase


class ComercioServices(Base):

    def create_comercio(self, comercio: ComercioBase):
        db_comercio = Comercio(**comercio.dict())
        self.db.add(db_comercio)
        self.db.commit()
        self.db.refresh(db_comercio)
        return db_comercio
    
    def get_comercios(self):
        return self.db.query(Comercio).all()
    