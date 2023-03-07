from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


Base = declarative_base()

engine = create_engine('sqlite:///DB/database.sqlite')


# Crea la tabla en la base de datos
Base.metadata.create_all(engine)
print("debe imprimir esto")
# Crea una sesion para interactuar con la base de datos
Session = sessionmaker(bind=engine)
print("debe imprimir esto")
session = Session()