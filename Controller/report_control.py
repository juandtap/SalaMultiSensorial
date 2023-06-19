# La clase Report realiza el proceso de enviar los datos de la sesion seleccionada
# a una plantilla en HTML la cual se convertira en PDF y permitira al usario
# descargarlo en el directorio que elija

# La clase GeneralReport envia los datos generales del estudiante y las sesiones trabajadas 
# hasta el momento a la otra plantilla HTML y luego a PDF

# La clase StudentListReport se usa para mostrar una lista de todos los estudiantes

import sys
import os, io
sys.path.append(".")
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtCore import Qt, QStandardPaths
from PIL import Image
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
        # se crea el diccionario para enviar datos adicionales que no estan en el objeto Student, como la edad y la foto
        
        flag_discapacidad = 'No'
        if self.student.discapacidad:
            flag_discapacidad = 'Si'
        
        # Recuperar la foto de la base de datos
        fotografia = self.student.fotografia
        
        if fotografia is not None:
            imagen = Image.open(io.BytesIO(fotografia))
             # extrae la extencion de la foto alamacenada (png, jpg, ...)
            extention = imagen.format.lower()
            photo_name = 'fotografia_estudiante'
            photo_path = os.path.join('Assets/SessionReports/', photo_name + '.' + extention)
            with open(photo_path, 'wb') as photo_file:
                photo_file.write(fotografia)
            
            print("Fotografia estudiante recuperada en : "+photo_path)
        else:
            print("estudiante sin fotografia")
            photo_name = "Sin Imagen"
            extention = ""
        
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
            'fecha_nacimiento': self.student.fecha_nacimiento.strftime("%d/%m/%Y"),
            'fotografia': (photo_name + '.' + extention),
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

        # agregar modulo de pictogramas
        
        plots_vumeter = PlotVumeter(student_sesion)
        vumeter_list = plots_vumeter.getPlotList()
        
        # Renderizar la plantilla html
        output = template.render(
            estudiante=student_info,
            sesion=student_sesion,
            modulos_trabajados=modulos,
            lista_vumetro=vumeter_list
        )
        
        # Guardar el resultado como archivo HTML
        with open('Assets/SessionReports/reporte.html', 'w') as file:
            file.write(output)
        
        
        # Codigo para guardar en una ruta especifica
        # HTML(string=output, base_url='SessionReports/').write_pdf('Assets/SessionReports/reportpdf.pdf')
        # print("reporte PDF generado")
        
        
        # codigo para abrir el explorador de archivos para guardar el reporte
        
        # Obtener la ruta por defecto de la carpeta "Descargas"
        default_folder = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
        default_pdf_name = os.path.join(
            default_folder,
            f"reporte_{self.student.apellidos}_{self.student.nombres}_sesion_{str(self.id_sesion)}.pdf"
        )

        
        docpdf = HTML(string=output, base_url='Assets/SessionReports/')
        
        options = QFileDialog.Options()
        
        # esta linea evita usar el dialogo nativo del SO
        #options |= QFileDialog.DontUseNativeDialog
        
        file_path, _ = QFileDialog.getSaveFileName(None, "Guardar Reporte PDF",default_pdf_name, "PDF (*.pdf)", options=options)
        
        if file_path:
            # Guardar el archivo PDF resultante en la ruta seleccionada
            if not file_path.lower().endswith(".pdf"):
                file_path += ".pdf"
            
            docpdf.write_pdf(file_path)

            print("reporte PDF guardado en :"+file_path)
            # retorna True si se presiono el boton de guardar de la ventana de dialogo del explorador de archivos
            return True
        else:
            return False
            
        
        
            
       
    def calculate_age(self, date):
        # Obtenemos la fecha actual
        current_date = date.today()
        
        # Calculamos la edad restando el año actual menos el año de nacimiento
        age = current_date.year - date.year
        
        # Si el cumpleaños de la persona aun no ha llegado en el anioo actual, se resta 1 a la edad
        if (current_date.month, current_date.day) < (date.month, date.day):
            age -= 1
            
        return age  


class GeneralReport:
    def __init__(self, student):
        self.student = student
        
    def download_general_report(self):
        print("Descargando reporte general pdf...")
        # Cargar la plantilla 
        env = Environment(loader=FileSystemLoader('Assets/plantilla_reportes'))
        template = env.get_template('general_session_report_template.html')
        
        flag_discapacidad = 'No'
        if self.student.discapacidad:
            flag_discapacidad = 'Si'
        
        # Recuperar la foto de la base de datos
        fotografia = self.student.fotografia
        if fotografia is not None:
            photo_name = 'fotografia_estudiante'
            # extrae la extencion de la foto alamacenada (png, jpg, ...)
            imagen = Image.open(io.BytesIO(fotografia))
            extention = imagen.format.lower()
        
            photo_path = os.path.join('Assets/SessionReports/', photo_name + '.' + extention)
            with open(photo_path, 'wb') as photo_file:
                photo_file.write(fotografia)
            
            print("Fotografia estudiante recuperada en : "+photo_path)
            
        else:
            print("estudiante sin fotografia")
            photo_name= "Sin imagen"
            extention = ""
            
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
            'fecha_nacimiento': self.student.fecha_nacimiento.strftime("%d/%m/%Y"),
            'fotografia': (photo_name + '.' + extention),
            'numero_sesiones': len(self.student.sesiones),
            'ultima_sesion': self.student.sesiones[-1].fecha.strftime("%d/%m/%Y") + "  "+
                            self.student.sesiones[-1].hora_inicio.strftime("%H:%M")+ " - "+
                            self.student.sesiones[-1].hora_fin.strftime("%H:%M")
        }
        
        # fecha y hora en la que se descarga el reporte general
        current_date = datetime.now()
        fecha_reporte = current_date.strftime("%d/%m/%Y %H:%M")
        
        # Renderizar la plantilla html
        output = template.render(
            estudiante=student_info,
            sesiones=self.student.sesiones,
            fecha_reporte = fecha_reporte,
        )
        
        # Guardar el resultado como archivo HTML
        with open('Assets/SessionReports/reporte_general.html', 'w') as file:
            file.write(output)
            
         # Obtener la ruta por defecto de la carpeta "Descargas"
        default_folder = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
        default_pdf_name = os.path.join(
            default_folder,
            f"reporte_general_{self.student.apellidos}_{self.student.nombres}.pdf"
        )

        
        docpdf = HTML(string=output, base_url='Assets/SessionReports/')
        
        options = QFileDialog.Options()
        
        # esta linea evita usar el dialogo nativo del SO
        #options |= QFileDialog.DontUseNativeDialog
        
        file_path, _ = QFileDialog.getSaveFileName(None, "Guardar Reporte PDF",default_pdf_name, "PDF (*.pdf)", options=options)
        
        if file_path:
            # Guardar el archivo PDF resultante en la ruta seleccionada
            if not file_path.lower().endswith(".pdf"):
                file_path += ".pdf"
            
            docpdf.write_pdf(file_path)

            print("reporte general PDF guardado en :"+file_path)
            # retorna True si se presiono el boton de guardar de la ventana de dialogo del explorador de archivos
            return True
        else:
            return False
        
        
    def calculate_age(self, date):
        # Obtenemos la fecha actual
        current_date = date.today()
        
        # Calculamos la edad restando el año actual menos el año de nacimiento
        age = current_date.year - date.year
        
        # Si el cumpleaños de la persona aun no ha llegado en el anioo actual, se resta 1 a la edad
        if (current_date.month, current_date.day) < (date.month, date.day):
            age -= 1
            
        return age  
    

class StudentListReport:
    def __init__(self, student_list):
        self.student_list = student_list
        
    def download_list(self):
        
       
        # fecha y hora en la que se descarga la lista 
        current_date = datetime.now()
       
        
        # Cargar la plantilla 
        env = Environment(loader=FileSystemLoader('Assets/plantilla_reportes'))
        template = env.get_template('student_list_template.html')
        
        # Renderizar la plantilla html
        output = template.render(
            estudiantes = self.student_list,
            fecha_reporte = current_date.strftime("%d/%m/%Y %H:%M"),
            numero_estudiantes = len(self.student_list)
        )
        
        # Guardar el resultado como archivo HTML
        with open('Assets/SessionReports/lista_estudiantes.html', 'w') as file:
            file.write(output)
            
         # Obtener la ruta por defecto de la carpeta "Descargas"
        default_folder = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
        default_pdf_name = os.path.join(
            default_folder,
            "lista_estudiantes.pdf"
        )

        
        docpdf = HTML(string=output, base_url='Assets/SessionReports/')
        
        options = QFileDialog.Options()
        
        file_path, _ = QFileDialog.getSaveFileName(None, "Guardar Lista Estudiantes PDF",default_pdf_name, "PDF (*.pdf)", options=options)
        
        if file_path:
            # Guardar el archivo PDF resultante en la ruta seleccionada
            if not file_path.lower().endswith(".pdf"):
                file_path += ".pdf"
            
            docpdf.write_pdf(file_path)

            print("lista de estudiantes PDF guardado en :"+file_path)
            # retorna True si se selecciona un lugar donde guardar, False si no
            return True
        else:
            return False