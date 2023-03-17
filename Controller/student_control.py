import sys
sys.path.append(".")
from Model.model import Estudiante,session
from Controller.discapacidad_control import get_discapacidad_by_name
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
    
    disc_list_objects = []
    for i in range(len(student_data[11])):
        disc_list_objects.append(get_discapacidad_by_name(student_data[11][i]))
    
    ## mostrar elementos prueba
    print("lista de objetos recuperada con get_discapacidad_by_name:")
    for i in range(len(disc_list_objects)):
        print(disc_list_objects[i].nombre_discapacidad)
        new_student.discapacidades.append(disc_list_objects[i])
    
    session.add(new_student)
    session.commit()
    session.close()
    return True
# Read
def get_all_students():
    student_list = session.query(Estudiante).all()
    return student_list

def get_student_by_id(student_id):
    student = session.query(Estudiante).filter_by(id=student_id).first()
    return student

def get_student_by_cedula(student_cedula):
    return session.query(Estudiante).filter_by(cedula=student_cedula).first()

# Busqueda de estudiantes por nombre o apellido

def get_student_by_names(search):
    pass