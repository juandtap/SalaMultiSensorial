import sys
sys.path.append(".")
from Model.model import Estudiante,session
from sqlalchemy import or_
from Controller.discapacidad_control import get_discapacidad_by_name
# defino los metodo CRUD para estudiante

# CREATE
# la funcion recibe una lista con los datos/atributos del estudiante
def add_student_control(student_data):
    
    if get_student_by_cedula(student_data[0]) is None:
        
        # convertir imagen a bytes
        # el string con el path de la imagen esta en la posicion 9 student_data[9]
        if student_data[9] is not None and student_data[9] != "":
            with open(student_data[9], "rb") as image_file:
                image_bytes = image_file.read()
        else: image_bytes = None
        new_student = Estudiante(
            cedula = student_data[0],
            apellidos = student_data[1].upper(), #str
            nombres = student_data[2].upper(), #str
            cedula_representante = student_data[3],
            nombre_representante = student_data[4].upper(), #str
            fecha_nacimiento = student_data[5], 
            direccion = student_data[6].upper(),  #str
            telefonos = student_data[7],
            discapacidad = student_data[8],
            fotografia = image_bytes, # imagen bytes
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
    else:
        return False
# READ
def get_all_students():
    student_list = session.query(Estudiante).filter(Estudiante.id != 1).all()
    # student_list = session.query(Estudiante).all()
    
    return student_list

def get_student_by_id(student_id):
    student = session.query(Estudiante).filter_by(id=student_id).first()
    
    return student

def get_student_by_cedula(student_cedula):
    student = session.query(Estudiante).filter_by(cedula=student_cedula).first()
    print(type(student))
    # no cerrar la sesion, error con dicapacidad
    return student

# Busqueda de estudiantes por nombre o apellido

def get_student_by_names(search_text):
    result_search = session.query(Estudiante).filter(Estudiante.nombres.like("%"+search_text+"%") |Estudiante.apellidos.like("%"+search_text+"%")).all()
    session.close()
    return result_search

# UPDATE

def update_student(student_id, new_student_data):
    student_to_update = session.query(Estudiante).filter_by(id=student_id).first()
    
    if new_student_data[9] is not None and new_student_data[9] != "":
        with open(new_student_data[9], "rb") as image_file:
            image_bytes = image_file.read()
    else: image_bytes = None
    student_to_update.cedula = new_student_data[0]
    student_to_update.apellidos = new_student_data[1].upper()  # str
    student_to_update.nombres = new_student_data[2].upper()  # str
    student_to_update.cedula_representante = new_student_data[3]
    student_to_update.nombre_representante = new_student_data[4].upper() # str
    student_to_update.fecha_nacimiento = new_student_data[5]
    student_to_update.direccion = new_student_data[6].upper()  # str
    student_to_update.telefonos = new_student_data[7]
    student_to_update.discapacidad = new_student_data[8]
    if image_bytes is not None:
        student_to_update.fotografia = image_bytes # image byte
    student_to_update.id_unidad_educativa = new_student_data[10]
    disc_list_objects = []
    for i in range(len(new_student_data[11])):
        disc_list_objects.append(get_discapacidad_by_name(new_student_data[11][i]))
        
        ## mostrar elementos prueba
    student_to_update.discapacidades.clear()
    print("lista de objetos recuperada con get_discapacidad_by_name:")
    for i in range(len(disc_list_objects)):
        print(disc_list_objects[i].nombre_discapacidad)
        student_to_update.discapacidades.append(disc_list_objects[i])
    
    session.commit()
    session.close()
    return True

# DELETE

def delete_student_by_id(student_id):
    student_to_delete = session.query(Estudiante).filter_by(id=student_id).first()
    if student_to_delete:
        session.delete(student_to_delete)
        session.commit()
        session.close()
        return True
    else:
        return False