import sys
sys.path.append(".")
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, LargeBinary
from Model.dbconection import Base
# aqui se definene las tablas de la base de datos

# tabla estudiante
class Student(Base):
    __tablename__ = 'Estudiante'
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
    extend_existing=True
    
