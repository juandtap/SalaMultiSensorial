import sys
sys.path.append(".")
from Model.model import Unidad_Educativa, session


# Create
def add_school_control(school_name):
    new_school = Unidad_Educativa(nombre = school_name)
    session.add(new_school)
    session.commit()
    session.close()
    return True

# Read

# metodo para obetener todas las unidades educativas y cargarlas al comboBox correspondiente

def get_all_schools():
    # schools es una lista de objetos 'Unidad_educativa
    school_list = session.query(Unidad_Educativa).all()
    return school_list