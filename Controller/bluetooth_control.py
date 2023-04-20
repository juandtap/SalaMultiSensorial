# este modulo es para obtener el puerto COM al que esta conectada
# la PC por bluetooth al modulo HC-05 con la direccion MAC 00:22:03:01:8A:12

import serial.tools.list_ports
import bluetooth

def find_port(mac_address):
    # Enumera todos los puertos seriales disponibles en el sistema
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        # Obtiene el nombre del dispositivo del puerto serial
        device = p.device
        # Busca la dirección MAC del dispositivo Bluetooth que corresponde al puerto serial
        try:
            device_info = bluetooth.lookup_name(mac_address, timeout=5)
            # if device_info is not None and device_info == p.hwid:
            if device_info is not None:
                return device
        except:
            pass
    # Devuelve None si no se encuentra ningún puerto correspondiente a la dirección MAC
    return None

#mac_address = '00:22:03:01:8A:12' # dirección MAC del modulo HC-05 (1)
mac_address = '00:22:03:01:7d:dc' # dirección MAC del modulo HC-05 (2)del modulo de grafomotricidad
port = find_port(mac_address)
if port is not None:
    print(f"El modulo HC-05 esta conectado al puerto {port}")
else:
    print("No se encuentra el puerto para el modulo HC-05")

# devices = bluetooth.discover_devices()
# for device in devices:
#     print(device)