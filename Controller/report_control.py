# La clase Report realiza el proceso de enviar los datos de la sesion seleccionada
# a una plantilla en HTML la cual se convertira en PDF y permitira al usario
# descargarlo en el directorio que elija

# La clase GeneralReport envia los datos generales del estudiante y las sesiones trabajadas 
# hasta el momento a la otra plantilla HTML y luego a PDF


import sys
sys.path.append(".")
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from Controller.student_control import get_student_by_id
from Controller.session_control import get_sesion_by_id
from Controller.plot_vum_control import PlotVumeter


class Report:
    def __init__(self, student, id_sesion):
        self.student = student
        self.id_sesion = id_sesion
        
    def download_report(self):
        print("Descargando reporte pdf...")
        # Cargar la plantilla 
        env = Environment(loader=FileSystemLoader('Assets/plantilla_reportes'))
        template = env.get_template('session_report_template.html')

        # creo un diccionario con los datos del estudiante, para enviarlos a la plantilla
        # se crea el diccionario para enviar datos adicionales que no estan en el objeto Student, como la edad
        
        flag_discapacidad = 'No'
        if self.student.discapacidad:
            flag_discapacidad = 'Si'

        student_info = {
            'cedula' : self.student.cedula,
            'apellidos': self.student.apellidos,
            'nombres' : self.student.nombres,
            'cedula_representante': self.student.cedula_representante,
            'representante': self.student.nombre_representante,
            'telefonos': self.student.telefonos,
            'direccion': self.student.direccion,
            'discapacidad': flag_discapacidad,
            'discapacidades': self.student.discapacidades,
            'edad': self.calculate_age(self.student.fecha_nacimiento),
            'fecha_nacimiento': self.student.fecha_nacimiento
        }
        
        # obtengo los modulos trabajados
        # agregar modulo de grafomotricidad
        student_sesion = get_sesion_by_id(self.id_sesion)
        modulos = ''

        if len(student_sesion.modulos_grafomotricidad) > 0:
            modulos += 'grafomotricidad,'
        if len(student_sesion.modulos_vumetro) > 0:
            modulos += ' vumetro,'
        if len(student_sesion.modulos_iluminacion) > 0:
            modulos += ' iluminación,'
      
    # aqui nos quedamos..
        
    def calculate_age(self, date):
        # Obtenemos la fecha actual
        current_date = date.today()
        
        # Calculamos la edad restando el año actual menos el año de nacimiento
        age = current_date.year - date.year
        
        # Si el cumpleaños de la persona aun no ha llegado en el anioo actual, se resta 1 a la edad
        if (current_date.month, current_date.day) < (date.month, date.day):
            age -= 1
            
        return age  
        
        

# Cargar la plantilla desde el sistema de archivos
env = Environment(loader=FileSystemLoader('Assets/plantilla_reportes'))
template = env.get_template('session_report_template.html')

# pruebas de reportes

# obtener estudiante
student = get_student_by_id(10)

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

student_sesion = get_sesion_by_id(39)

# obtengo los modulos trabajados

modulos = ''

if len(student_sesion.modulos_grafomotricidad) > 0:
    modulos += 'grafomotricidad,'
if len(student_sesion.modulos_vumetro) > 0:
    modulos += ' vumetro,'
if len(student_sesion.modulos_iluminacion) > 0:
    modulos += ' iluminación,'

# enviar array de path de las imagenes del plot del modulo vumetro

vumetro_list = lista_plots

# Renderizar la plantilla con el objeto como variable de contexto
output = template.render(estudiante=student_info,sesion=student_sesion,modulos_trabajados=modulos,lista_vumetro=vumetro_list)

# Guardar el resultado como archivo HTML
with open('SessionReports/reporte1.html', 'w') as file:
    file.write(output)
    
    

# Convertir el archivo HTML a PDF
## HTML(filename='/SessionReports/reporte1.html').write_pdf('reporte1.pdf')


HTML(string=output, base_url='SessionReports/').write_pdf('SessionReports/pdfreport2.pdf')
print("reporte PDF generado")