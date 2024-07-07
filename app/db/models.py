from app.db.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean, Time
from sqlalchemy.orm import relationship



class Comercio(Base):
    __tablename__ = 'comercios'
    id_comercio = Column(Integer, primary_key=True, index=True)
    nom_comercio = Column(String, index=True)
    aforo_maximo = Column(Integer)

    servicios = relationship("Servicio", back_populates="comercio")

class Servicio(Base):
    __tablename__ = 'servicios'
    id_servicio = Column(Integer, primary_key=True, index=True)
    id_comercio = Column(Integer, ForeignKey('comercios.id_comercio'))
    nom_servicio = Column(String, index=True)
    hora_apertura = Column(Time)
    hora_cierre = Column(Time)
    duracion = Column(Integer)

    comercio = relationship("Comercio", back_populates="servicios")
    turnos = relationship("Turno", back_populates="servicio")

class Turno(Base):
    __tablename__ = 'turnos'
    id_turno = Column(Integer, primary_key=True, index=True)
    id_servicio = Column(Integer, ForeignKey('servicios.id_servicio'))
    fecha_turno = Column(Date)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    estado = Column(Boolean, default=True)

    servicio = relationship("Servicio", back_populates="turnos")