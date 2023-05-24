import sys
sys.path.append(".")
# import os
# os.add_dll_directory(r'C:\\msys64\\mingw64\\bin')
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from Controller.student_control import get_student_by_id
from Controller.session_control import get_sesion_by_id
# Cargar la plantilla desde el sistema de archivos
env = Environment(loader=FileSystemLoader('Assets/plantilla_reportes'))
template = env.get_template('session_report_template.html')

# pruebas de reportes

# obtener estudiante
student = get_student_by_id(1)

# creo un diccionario con los datos del estudiante

def calculate_age(date):
        # Obtenemos la fecha actual
        current_date = date.today()
    
        # Calculamos la edad restando el año actual menos el año de nacimiento
        age = current_date.year - date.year
    
        # Si el cumpleaños de la persona aun no ha llegado en el anioo actual, se resta 1 a la edad
        if (current_date.month, current_date.day) < (date.month, date.day):
            age -= 1
        
        return age

flag_discapacidad = 'No'
if student.discapacidad:
    flag_discapacidad = 'Si'

student_info = {
    'cedula' : student.cedula,
    'apellidos': student.apellidos,
    'nombres' : student.nombres,
    'cedula_representante': student.cedula_representante,
    'representante': student.nombre_representante,
    'telefonos': student.telefonos,
    'direccion': student.direccion,
    'discapacidad': flag_discapacidad,
    'discapacidades': student.discapacidades,
    'edad': calculate_age(student.fecha_nacimiento),
    'fecha_nacimiento': student.fecha_nacimiento
}

# obtengo una sesion asociada al estudiante (16)

student_sesion = get_sesion_by_id(16)

# obtengo los modulos trabajados

modulos = ''

if len(student_sesion.modulos_grafomotricidad) > 0:
    modulos += 'grafomotricidad'
if len(student_sesion.modulos_vumetro) > 0:
    modulos += ', vumetro'
    


# Renderizar la plantilla con el objeto como variable de contexto
output = template.render(estudiante=student_info,sesion=student_sesion,modulos_trabajados=modulos)

# Guardar el resultado como archivo HTML
with open('SessionReports/reporte1.html', 'w') as file:
    file.write(output)
    
    

# Convertir el archivo HTML a PDF
## HTML(filename='/SessionReports/reporte1.html').write_pdf('reporte1.pdf')


HTML(string=output, base_url='SessionReports/').write_pdf('SessionReports/pdfreport1.pdf')
print("reporte PDF generado")