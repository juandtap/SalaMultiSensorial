import sys
sys.path.append(".")
from Model.model import Student
from Model.dbconection import session
# defino los metodo CRUD para estudiante

# Create
def add_student_control(dato1, dato2, dato3):
    student = Student(cedula=dato1, apellidos=dato2, nombres=dato3)
    session.add(student)
    session.commit()
    session.close()
    return True
# Read
def get_student_list():
    student_list = session.query(Student).all()
    return student_list