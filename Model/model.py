import sys
sys.path.append(".")
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from Model.dbconection import Base
# aqui se definene las tablas de la base de datos

# tabla estudiante
class Estudiante(Base):
    __tablename__ = 'estudiante'
    id = Column(Integer, primary_key=True)
    cedula = Column(String(10))
    apellidos = Column(String(50))
    nombres = Column(String(50))
    cedula_representante = Column(String(10))
    nombre_representante = Column(String(100))
    fecha_nacimiento = Column(Date)
    direccion = Column(String(100))
    telefonos = Column(String(100))
    discapacidad = Column(Boolean, default=False)
    fotografia = Column(LargeBinary)
    id_unidad_educativa = Column(Integer, ForeignKey('unidad_educativa.id'))
    # unidad_educativa = relationship("Unidad_Educativa", back_populates="estudiantes")
    # extend_existing=True
    
# tabla Unidad_educativa
class Unidad_Educativa(Base):
    __tablename__ = 'unidad_educativa'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    estudiantes = relationship('Estudiante', backref='unidad_educativa')
    
