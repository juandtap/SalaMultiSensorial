# este modulo es para obtener el puerto COM al que esta conectada
# la PC por bluetooth
# !!!!aun no se prueba !!!!
import bluetooth

target_name = "NombreDelDispositivoBluetooth"
target_address = None

# Buscamos dispositivos Bluetooth cercanos
nearby_devices = bluetooth.discover_devices()

# Buscamos el dispositivo con el nombre especificado
for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

# Si encontramos el dispositivo, buscamos el puerto COM al que está conectado
if target_address is not None:
    services = bluetooth.find_service(address=target_address)
    for svc in services:
        if svc['name'] == "Serial Port":
            port = svc['port']
            print(f"El dispositivo {target_name} está conectado al puerto COM {port}")
else:
    print(f"No se pudo encontrar el dispositivo {target_name}")

