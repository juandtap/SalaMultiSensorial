import sys
sys.path.append(".")
from Model.model import Estudiante,session

# defino los metodo CRUD para estudiante

# Create
# la funcion recibe una lista con los datos/atributos del estudiante
def add_student_control(student_data):
    
    new_student = Estudiante(
        cedula = student_data[0],
        apellidos = student_data[1],
        nombres = student_data[2],
        cedula_representante = student_data[3],
        nombre_representante = student_data[4],
        fecha_nacimiento = student_data[5],
        direccion = student_data[6],
        telefonos = student_data[7],
        discapacidad = student_data[8],
        fotografia = student_data[9],
        id_unidad_educativa = student_data[10]
    )
    session.add(new_student)
    session.commit()
    session.close()
    return True
# Read
def get_student_list():
    student_list = session.query(Estudiante).all()
    return student_list