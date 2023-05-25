# este modulo py es para probar el plotting de los datos guardados del vumetro
import json
import matplotlib.pyplot as plt
import sys
sys.path.append(".")

from Controller.session_control import get_sesion_by_id

sesion_estudiante = get_sesion_by_id(39)

modulos_vumetro = sesion_estudiante.modulos_vumetro

# datos_vum es un objeto de tipo ModuloVumetro
# se accede al path de los datos (JSON) con datos_vum.datos

lista_plots = []

for i, datos_vum in enumerate(modulos_vumetro):        

    # Leer los datos del archivo JSON para el eje Y
    with open(datos_vum.datos, 'r') as file:
        datos_y = json.load(file)

    # Generar valores para el eje X en una secuencia de 50 en 50 ms
    datos_x = [50 * i for i in range(len(datos_y))]

    # Crear el gráfico
    plt.plot(datos_x, datos_y)
    plt.xlabel('Tiempo (50ms)')
    plt.ylabel('Nivel')

    nombre_plot = f"plot_vumetro_{i+1}.png"
    lista_plots.append(nombre_plot)
    # Guardar la imagen como archivo
    plt.savefig('SessionReports/'+nombre_plot)
    print("Grafica "+str(i+1)+" creada")
    plt.clf()
    # Mostrar el gráfico en pantalla (opcional)
    #plt.show()

print(lista_plots)
print(len(lista_plots))