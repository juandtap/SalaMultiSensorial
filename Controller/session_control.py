import sys
sys.path.append(".")

from Model.model import session, Sesion
# Sesion es la clase
# session es la sesion de la conexion con la base de datos
# Create 

def add_sesion_module(new_sesion, new_module):
    flag = False
    session.add_all([new_sesion,new_module])
    session.commit()
    session.close()
    flag = True
    return flag
    
# Read

def get_sesion_by_id(id_sesion):
    return session.query(Sesion).filter_by(id=id_sesion).first()
