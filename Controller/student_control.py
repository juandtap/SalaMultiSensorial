import sys
sys.path.append(".")
from Model.model import Estudiante,session

# defino los metodo CRUD para estudiante

# Create
def add_student_control(dato1, dato2, dato3):
    student = Estudiante()
    session.add(student)
    session.commit()
    session.close()
    return True
# Read
def get_student_list():
    student_list = session.query(Estudiante).all()
    return student_list