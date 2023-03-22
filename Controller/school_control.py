import sys
sys.path.append(".")
from Model.model import Unidad_Educativa, session


# Create
def add_school_control(school_name):
    if get_school_by_name(school_name.strip().upper()) is None:
        new_school = Unidad_Educativa(nombre = school_name.strip().upper())
        session.add(new_school)
        session.commit()
        session.close()
        return True
    else:
        return False
# Read

# metodo para obetener todas las unidades educativas y cargarlas al comboBox correspondiente

def get_all_schools():
    # schools es una lista de objetos 'Unidad_educativa
    school_list = session.query(Unidad_Educativa).all()
    return school_list

def get_school_by_id(school_id):
    return session.query(Unidad_Educativa).filter_by(id=school_id).first()

def get_school_by_name(school_name):
    return session.query(Unidad_Educativa).filter_by(nombre=school_name).first()
