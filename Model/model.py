import sys
sys.path.append(".")
from sqlalchemy import create_engine, Column, Integer, String
from Model.dbconection import Base
# aqui se definene las tablas de la base de datos

# tabla estudiante
class Student(Base):
    __tablename__ = 'Estudiante'
    id = Column(Integer, primary_key=True)
    cedula = Column(String(10))
    apellidos = Column(String(50))
    nombres = Column(String(50))
    extend_existing=True
    
