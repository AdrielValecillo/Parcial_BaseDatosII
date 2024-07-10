from app.services.base import Base
from app.db.models import Turno, Servicio, Comercio
from app.api.schemas.schemas_turnos import TurnoBase
from sqlalchemy.orm import joinedload
from datetime import datetime, timedelta
from typing import List

class TurnoServices(Base):

    def generate_turno(self, turno: TurnoBase) -> List[Turno]:
            # Convertir las fechas de string a objetos datetime
        fecha_inicio = turno.fecha_inicio
        fecha_fin = turno.fecha_fin
        # Consultar el servicio
        servicio = self.db.query(Servicio).filter(Servicio.id_servicio == turno.id_servicio).first()
        if not servicio:
            return "Servicio no encontrado"
        
        turnos_generados = []
        delta = timedelta(days=1)
        fecha_actual = fecha_inicio
        
        while fecha_actual <= fecha_fin:
            hora_actual = servicio.hora_apertura
            while hora_actual < servicio.hora_cierre:
                # Calcular la hora de fin del turno actual
                fin_turno = (datetime.combine(fecha_actual, hora_actual) + timedelta(minutes=servicio.duracion)).time()
                
                # Asegurarse de no exceder la hora de cierre
                if fin_turno > servicio.hora_cierre:
                    break
                
                # Crear y almacenar el turno
                nuevo_turno = Turno(id_servicio=turno.id_servicio, hora_inicio=hora_actual, 
                                    hora_fin=fin_turno, fecha_turno=fecha_actual, estado=True)
                self.db.add(nuevo_turno)
                self.db.commit()
                
                turnos_generados.append(nuevo_turno)
                
                # Preparar la siguiente iteración
                hora_actual = fin_turno
            
            fecha_actual += delta
        
        return turnos_generados
    
    def get_last_turno(self, nom_comercio: str):
        last_turno = self.db.query(Turno).join(Servicio).join(Comercio).filter(
            Comercio.nom_comercio == nom_comercio).order_by(
                Turno.id_turno.desc()).first()
        return last_turno