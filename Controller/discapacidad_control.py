import sys
sys.path.append(".")
from Model.model import Discapacidad, session

# Create

def add_discapacidad_control(dis_name):
    
    new_discapacidad = Discapacidad(nombre_discapacidad = dis_name.upper())
    session.add(new_discapacidad)
    session.commit()
    session.close()
    return True


# Read

def get_all_discapacidades():
    discapacidades_list = session.query(Discapacidad).all()
    return discapacidades_list

def get_discapacidad_by_id(dis_id):
    return session.query(Discapacidad).filter_by(id=dis_id).first()

def get_discapacidad_by_name(dis_name):
    return session.query(Discapacidad).filter_by(nombre_discapacidad=dis_name).first()