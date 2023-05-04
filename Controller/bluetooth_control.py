# modulo de pruebas para la conexion con el modulo hc05 mediante socket bluetooth
# mac_address = '00:22:03:01:8A:12' # dirección MAC del modulo HC-05 (1)
# #mac_address = '00:22:03:01:7D:DC' # dirección MAC del modulo HC-05 (2)del modulo de grafomotricidad


import bluetooth

mac_hc05_testing = '00:22:03:01:8A:12'
mac_hc05_grafomotricidad = '00:22:03:01:7D:DC'

addr = mac_hc05_testing

# Conectar al dispositivo
sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
sock.connect((addr, 1))

# Enviar datos al dispositivo
sock.send('Hola, HC05!')

while True:
# Recibir datos del dispositivo
    data = sock.recv(1024)
    print(data)

# Cerrar la conexión
sock.close()

