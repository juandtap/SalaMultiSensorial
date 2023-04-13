# este modulo es para obtener el puerto COM al que esta conectada
# la PC por bluetooth
# !!!!aun no se prueba !!!!
# import bluetooth

# target_name = "HC-05"
# target_address = None

# # Buscamos dispositivos Bluetooth cercanos
# nearby_devices = bluetooth.discover_devices()

# # Buscamos el dispositivo con el nombre especificado
# for bdaddr in nearby_devices:
#     if target_name == bluetooth.lookup_name( bdaddr ):
#         target_address = bdaddr
#         break

# # Si encontramos el dispositivo, buscamos el puerto COM al que está conectado
# if target_address is not None:
#     services = bluetooth.find_service(address=target_address)
#     for svc in services:
#         if svc['name'] == "Serial Port":
#             port = svc['port']
#             print(f"El dispositivo {target_name} está conectado al puerto COM {port}")
# else:
#     print(f"No se pudo encontrar el dispositivo {target_name}")

# import bluetooth

# # Busca todos los dispositivos Bluetooth cercanos
# devices = bluetooth.discover_devices()

# # Busca los puertos COM a los que están conectados los dispositivos Bluetooth
# for device in devices:
#     print(f"Buscando puertos COM para el dispositivo: {device}")
#     services = bluetooth.find_service(address=device)
#     for service in services:
#         if service["service-id"] == "Serial Port":
#             print(f"Dispositivo Bluetooth encontrado en el puerto COM: {service['port']}")


# import serial.tools.list_ports

# ports = serial.tools.list_ports.comports()

# for port in ports:
#     print(port.pid)
    
import bluetooth

addr = '00:22:03:01:8A:12'  # Dirección MAC del HC-05 4C:34:88:B5:29:25
port = None

# Busca los servicios disponibles en el dispositivo remoto
services = bluetooth.find_service(address=addr)

# Itera a través de los servicios buscando el puerto RFCOMM
for s in services:
    if s['protocol'] == 'RFCOMM':
        port = s['port']
        break

if port:
    print('El HC-05 está conectado al puerto COM', port)
else:
    print('No se encontró el puerto COM del HC-05')




