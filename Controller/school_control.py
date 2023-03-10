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