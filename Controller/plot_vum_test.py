# este modulo py es para probar el plotting de los datos guardados del vumetro
import json
import matplotlib.pyplot as plt
import sys
sys.path.append(".")
# Leer los datos del archivo JSON para el eje Y
with open('ModuleData/DatosVumetro/50_2023-05-23_12-53-12_datavum.json', 'r') as file:
    datos_y = json.load(file)

# Generar valores para el eje X en una secuencia de 50 en 50 ms
datos_x = [50 * i for i in range(len(datos_y))]

# Crear el gráfico
plt.plot(datos_x, datos_y)
plt.xlabel('Tiempo (ms)')
plt.ylabel('Nivel')


# Guardar la imagen como archivo
plt.savefig('SessionReports/plot_vumetro.png')
print("Grafica creada")
# Mostrar el gráfico en pantalla (opcional)
plt.show()
