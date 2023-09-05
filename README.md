# Aplicación de control de la Sala Multisensorial del Tambo
### Proyecto para el Centro de Ayuda Integral Psicopedagogica "ENTRA EN MI MUNDO"
### Programado por Diego Tapia, jtapiav4@est.ups.edu.ec
## 1 Requisitos
Para ejecutar la aplicación se necesita que este en Windows 10 ya que el bluetooth de Windows 11 no reconoce los dispositivos HC-05 de los módulos de la sala multisensorial.
Si se quiere usar en Windows 11 use un adaptador bluetooth (usb) para conectarse con los dispositivos HC-05.
### 1.1 Aplicaciones
Para ejecutar la aplicación desarrollada en Python desde un entorno de programacion o IDE, se necesita de las siguientes aplicaciones:

**Python 3.9** en adelante. Esto es debido a que la librería para la conexión bluetooth “pybluez2” es compatible en Windows solo en versiones de Python iguales o superiores a la 3.9 (https://pypi.org/project/pybluez2/ )

**Microsoft Visual C++ 2015**. Para desarrollar las interfaces graficas en Python se usó la librería PyQt5, para que no presente errores a la hora de instalar se debe de tener instalado el Microsoft Visual C++ 2015

**GTK 3 runtime**. La aplicación genera reportes en PDF a partir de una plantilla HTML con la librería Weasyprint, la cual necesita que se tenga instalado la aplicación gtk3
Se puede descargar del siguiente enlace: 
https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases

**Nota.** En la PC de la Sala Multisensorial se usa un .exe generado con la libreria ```pyinstaller``` para ejecutar la aplicacion solo tiene que estar instalado gtk3, cuyo enlace de descarga se indico anteriormente), si por alguna razón no funciona, instalar también Microsoft Visual C++ 2015.


### 1.2 Librerías Python.
**PyQt5.** Para el desarrollo de las interfaces graficas

**Pyqt5-tools** (opcional). Esta librería instala la herramienta Qtdesigner, que es la que se uso para el desarrollo de las interfaces gráficas de una manera más cómoda y rápida, se puede ejecutar la aplicación desde la siguiente carpeta: 
 ```C:/~/Python39/Lib/site-packages/qt5_applications/Qt/bin```
 
Esta aplicación guarda un archivo en con extencion .ui, la cual puede ser convertida a .py con el siguiente comando (ejecutar en el cmd o powershell en la ubicación del archivo .ui):

```pyuic5 nombrearchivo.ui -o nombrearchivopython.py```

Este paso es opcional, se puede desarrollar las interfaces graficas con código usando la librería PyQt5.
Nota. Se adjuntan los archivos .ui en caso se necesiten en la carpeta de OneDrive de la Catedra junto con el manual tecnico

**Sqlalchemy**. Esta librería es un ORM para gestionar la base de datos, la base de datos es sqlite.
Nota. Se puede usar directamente sentencias SQL si llegase a ser necesario.

**Pybluez2.** Para la conexión bluetooth. Para conectarse con los módulos HC05 se usa la dirección MAC del dispositivo por lo que no se usa el puerto COM y por lo tanto no se usa la librería pyserial.

**Jinja2**. Se usa para crear plantillas HTML para mostrar los reportes, estas plantillas son convertidas a PDF con la siguiente librería.

**Weasyprint**. Para convertir la plantilla HTML a PDF. (recordar tener instalado gtk3)

**Pyinstaller**. Se usa para generar un archivo ejecutable de la aplicación (exe) el comando que se usa es:

```pyinstaller main.py --onefile -w```


Estas librerías pueden instalar librerías adicionales, a continuación, se muestra la salida del comando ```pip freeze``` el cual tiene todas las librerías instaladas en la versión o ambiente virtual de Python.

```
altgraph==0.17.3
autopep8==2.0.2
Brotli==1.0.9
cffi==1.15.1
click==8.1.3
colorama==0.4.6
contourpy==1.0.7
cssselect2==0.7.0
cycler==0.11.0
fonttools==4.39.3
fpdf==1.7.2
greenlet==2.0.2
html5lib==1.1
importlib-resources==5.12.0
Jinja2==3.1.2
kiwisolver==1.4.4
MarkupSafe==2.1.2
matplotlib==3.7.1
numpy==1.24.2
packaging==23.1
pdfkit==1.0.0
pefile==2023.2.7
Pillow==9.5.0
platformdirs==3.2.0
protobuf==4.22.3
pybluez2==0.46
pycodestyle==2.10.0
pycparser==2.21
pydyf==0.6.0
pyinstaller==5.11.0
pyinstaller-hooks-contrib==2023.3
pyparsing==3.0.9
pyphen==0.14.0
PyQt5==5.15.9
pyqt5-plugins==5.15.9.2.3
PyQt5-Qt5==5.15.2
PyQt5-sip==12.12.0
pyqt5-tools==5.15.9.3.3
pyqtgraph==0.13.3
pyserial==3.5
python-dateutil==2.8.2
python-dotenv==1.0.0
pytoolconfig==1.2.5
pywin32-ctypes==0.2.0
qt5-applications==5.15.2.2.3
qt5-tools==5.15.2.1.3
rope==1.7.0
screeninfo==0.8.1
six==1.16.0
SQLAlchemy==2.0.9
tinycss2==1.2.1
tomli==2.0.1
typing_extensions==4.5.0
weasyprint==59.0
webencodings==0.5.1
zipp==3.15.0
zopfli==0.2.2

```
Tener en cuenta que no todas las librerías mostradas se usaron el proyecto. Se recomienda trabajar con ambientes virtuales.

## 2. Ejecución de la aplicación.
### 2.1 Ejecución desde el entorno de desarrollo
Para ejecutar la aplicación usando cualquier IDE Python o editor como Visual Code, una vez se tenga todas las librerías y aplicaciones requeridas se debe ejecutar el archivo ```main.py```
### 2.2 Ejecución desde el archivo ejecutable.
Después de generar el archivo ejecutable con el comando: 

```pyinstaller main.py --onefile -w```

**Nota.** Es muy importante ejecutar el anterior comando con esos parámetros, ```-w```; significa que será una app con interface gráfica y ```--onefile``` que se generará solo un archivo (el .exe)

En la raíz del proyecto se crea la carpeta “dist” que contendrá el archivo main.exe.



La carpeta dist no está el repositorio github porque está siendo ignorada por git para ahorrar espacio del repositorio ya que él .exe pesa alrededor de 70mb
Para que la aplicación funcione correctamente en la capeta donde está el archivo main.exe debe estar tres carpetas:

* Assets: que tiene las imágenes que usa la aplicación además de las plantillas en html (no borrar)
* DB: donde está el archivo de base de datos sqlite
* ModuleData: donde se guarda la información del vúmetro en archivos JSON necesaria para graficar los datos del vúmetro al momento de mostrar el reporte. 

Copiar estas carpetas (del proyecto) junto con el archivo main.exe en una carpeta aparte Y ejecutar el archivo. Se demora unos segundos en iniciar.

**Nota.** En la PC donde se va a ejecutar la aplicación no hace falta que este instalado Python, solo tiene que estar instalado gtk3, cuyo enlace de descarga se indico anteriormente, si por alguna razón no funciona, instalar también Microsoft Visual C++ 2015

## 3. Estructura del proyecto

### 3.1 Assets
El directorio Assets tiene todas las imágenes que se usan en la aplicación, también los archivos .html para la generación de reportes y las imágenes de las gráficas generadas con los datos del vúmetro. 
En el directorio SessionsReports están las imágenes que usaran los archivos html para mostrar el reporte, estos archivos tanto .png como .html se sobrescribirán conforme se vayan generando los reportes en pdf, los archivos de esta carpeta pueden eliminarse si se considera necesario ya que este directorio es la salida de las funciones que generan la plantilla html con las gráficas del vúmetro y la fotografia del estudiante, como se mencionó anteriormente estos archivos se sobrescriben por lo que no hace falta borrarlos a menos que se quiera ahorrar espacio en el repositorio de github.
Si se quiere reemplazar rápidamente una imagen, usar el mismo nombre que tiene dentro del directorio Assets.

### 3.2 Controller
En este directorio están los archivos que se usan para lo siguiente:
* Guardar los datos en la Base de Datos; ```report_control.py, school_control.py, session_control.py, discapacidad_control.py y student_control.py```
 * Generar las gráficas con los datos del vúmetro; ```plot_vum_control.py```
* Generar el archivo html que posteriormente será convertido a pdf ```report_control.py```
* Hilo que envía señales de inicio y fin para el control de los módulos, se usa en los módulos de grafomotricidad, vúmetro e iluminación, este hilo se ejecuta al abrir y cerrar la ventana del módulo respectivo ```modules_control.py```
* Archivo con diccionarios donde se especifican las direcciones MAC de los módulos bluetooth HC-05, path de las imágenes y códigos de las figuras para el módulo de grafomotricidad, y códigos RGB para el módulo de iluminación.

### 3.3 Model
En este directorio está el archivo model.py donde se especifican las clases del modelo de base de datos, usando la librería SQLalchemy

Si en algún momento se requiere agregar otro modulo crear la clase en el archivo model.py  y  agregarlo en la clase sesión como una relación, tal como se ve en la siguiente codigo con los modulos de grafomotricidad y vumetro:

```
class Sesion(Base):
    __tablename__ = 'sesion'
    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    id_estudiante = Column(Integer, ForeignKey('estudiante.id'))
    modulos_grafomotricidad = relationship('ModuloGrafomotricidad', backref='sesion', cascade="all, delete")
    modulos_vumetro = relationship('ModuloVumetro', backref='sesion', cascade="all, delete")
    modulos_iluminacion = relationship('ModuloIluminacion', backref='sesion', cascade="all, delete")
    modulos_pictogramas = relationship('ModuloPictogramas', backref='sesion', cascade="all, delete")
    
class ModuloGrafomotricidad(Base):
    __tablename__ = 'modulo_grafomotricidad'
    id = Column(Integer, primary_key=True)
    id_sesion = Column(Integer, ForeignKey('sesion.id'))
    figura = Column(String(50))
    tiempo_tomado = Column(Time)
    resultado = Column(String(20))
    
class ModuloVumetro(Base):
    __tablename__ = 'modulo_vumetro'
    id = Column(Integer, primary_key=True)
    id_sesion = Column(Integer, ForeignKey('sesion.id'))
    nivel_maximo = Column(Integer)
    nivel_promedio = Column(Integer)
    tiempo = Column(String(50))
    datos = Column(String(250))
```
Se puede usar otro ORM si se considera necesario.

### 3.4 DB
En este directorio se guarda el archivo de la base de datos (SQLite), si por algún motivo la base es eliminada, no hace falta crearla manualmente, la aplicación la crea si es que no detecta ningún archivo de base de datos.

### 3.5 ModuleData
En este directorio se guardan los archivos JSON que contienen la información recibida por el módulo del Vumetro, en la base de datos se guarda el path del archivo JSON, muy importante no borrar, ya que se requiere de estos para generar la gráfica (plot) a mostrar en el reporte pdf.

### 3.6 View
En este directorio se guarda los archivos .py de las ventanas de la aplicación, también los archivos que controlan estas ventanas. 

Las ventanas fueron desarrolladas usando la herramienta Designer.exe instalada con la librería PyQt-tools (revisar sección 1.2), también se pueden hacer usando solo código.
Todos los archivos que terminan con _view.py son archivos que contienen solo el código para la ventana o interfaz gráfica, si se quiere cambiar algo de la ventana como tamaño fuente de las letras, ubicación de los elementos, agregar o eliminar botones, etc., se debe modificar estos ya sea por código o usando la herramienta con los archivos .ui correspondientes (los archivos .ui se adjuntan junto con este documento)

En cuanto a la lógica se controla desde otros archivos, a continuación, se muestra una tabla donde se indica que archivos controlan a los archivos de interfaz gráfica.

| Archivo                | Controla a                   |
|------------------------|------------------------------|
| ```components.py```        | ```add_discapacidad_view.py```   |
| ```components.py```        | ```add_school_view.py```         |
| ```main.py```              | ```add_student_view.py```        |
| ```components.py```        | ```confirm_dialog_view.py```     |
| ```components.py```        | ```edit_student_view.py```       |
| ```main.py```              | ```main_window_view.py```        |
| ```components.py```        | ```message_dialog_view.py```     |
| ```module_components.py``` | ```module_selection_view.py```   |
| ```module_components.py``` | ```module_grafomotricidad_view.py``` |
| ```module_components_2.py```| ```module_iluminacion_view.py``` |
| ```module_components_3.py```| ```module_vumetro_view.py```     |
| ```module_components_4.py```| ```module_pictogram_view.py```   |
| ```components.py```        | ```student_list_view.py```       |
| ```components_2.py```      | ```student_report_view.py```     |

## 4 Envio y recepcion de datos por bluetooth
Los datos se envían y reciben usando sockets bluetooth con la librería ```pybluez2```, especificando la dirección MAC del módulo, para esto se utiliza un diccionario del archivo ```Controller/module_codes.py``` donde se especifica el número del módulo y nos devuelve la dirección MAC, la numeración es la siguiente:
| Numero | Modulo         |
|--------|----------------|
| 1      | Grafomotricidad|
| 2      | Vúmetro        |
| 3      | Iluminación    |
| 4      | Pictogramas    |

Cuando se quiere recibir datos de algún modulo, especificamos el número y establecemos conexión con él, por ejemplo:
```
def run(self):
    print("se ejecuta el hilo de escucha socket bluetooth")
    try:
        blue_socket = bluetooth.BluetoothSocket()
        blue_socket.connect((module_mac_address[1],1))
    except Exception as e:
        print("Error al intentar la conexion con HC05:", e)
        self.finished.emit()
        return
```
El segundo argumento en la función connect es el puerto bluetooth, ```connect(direccionMAC, puerto )```, el puerto a usar el ```1``` en todos los módulos.

Todas las funciones de enviar y recibir datos se ejecutan en QThreads, para no interrumpir la interfaz gráfica. Cada QThread está en el mismo archivo que controla la ventana del módulo correspondiente ya que de cada módulo se recibe o envia los datos de forma diferente

### Para mas información consultar el manual técnico
