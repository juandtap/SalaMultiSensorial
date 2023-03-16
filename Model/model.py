import sys
sys.path.append(".")
from sqlalchemy import create_engine, Table, Column, Integer, String, Date, Boolean, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///DB/database.sqlite')



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
    
    discapacidades = relationship('Discapacidad',secondary='estudiante_discapacidad', back_populates='estudiantes')
    # unidad_educativa = relationship("Unidad_Educativa", back_populates="estudiantes")
    # extend_existing=True
    
# tabla Unidad_educativa
class Unidad_Educativa(Base):
    __tablename__ = 'unidad_educativa'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    estudiantes = relationship('Estudiante', backref='unidad_educativa')

class Discapacidad(Base):
    __tablename__ = 'discapacidad'
    id = Column(Integer, primary_key=True)
    nombre_discapacidad = Column(String(100))
    
    estudiantes = relationship('Estudiante',secondary='estudiante_discapacidad',back_populates='discapacidades')



estudiante_discapacidad = Table('estudiante_discapacidad', Base.metadata,
    Column('estudiante_id', Integer, ForeignKey('estudiante.id')),
    Column('discapacidad_id', Integer, ForeignKey('discapacidad.id'))
)

# Crea las tablas en la base de datos
Base.metadata.create_all(engine)

# Crea una sesion para interactuar con la base de datos
Session = sessionmaker(bind=engine)

session = Session()
print("Modelo DB ejecutado/actualizado")