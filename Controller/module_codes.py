# diccionario con las direcciones MAC de los modulos HC05

# module_mac_address = {
#      0:'00:22:03:01:8A:12',  # HC05 de prueba
#      1:'00:22:03:01:7D:DC',  # HC05 del modulo grafomotricidad
#      2:'00:22:03:01:8D:B5', # HC05 del vumetro
     
#      3:'00:22:03:01:8A:12', # HC05 de prueba
#      4:'00:22:03:01:8A:12' # HC05 de prueba
# }

# para pruebas, comentar a la hora de probar con los modulos
module_mac_address = {
     0:'00:22:03:01:8A:12',  
     1:'00:22:03:01:8A:12', 
     2:'00:22:03:01:8A:12', 
     3:'00:22:03:01:8A:12', 
     4:'00:22:03:01:8A:12' 
}



# diccionario figuras del modulo
codigo_figuras = {
     
     1: 'cuadrado',
     2: 'circulo',
     3: 'triangulo',
     4: 'tortuga',
     5: 'oveja',
     6: 'vaca',
     7: 'cuadrado mediano',
     8: 'circulo mediano',
     9: 'triangulo mediano',
     10: 'perro',
     11: 'cerdo',
     12: 'gato',
     13: 'cuadrado pequeño',
     14: 'circulo pequeño',
     15: 'triangulo pequeño',
     16: 'gallina',
     17: 'caballo',
     18: 'conejo',
     
}
   
# lista con el path de las imagenes para el modulo de grafomotridad
path_figuras = [
     'Assets/grafomotricidad/01_cuadrado.png',
     'Assets/grafomotricidad/02_circulo.png',
     'Assets/grafomotricidad/03_triangulo.png',
     'Assets/grafomotricidad/04_tortuga.png',
     'Assets/grafomotricidad/05_oveja.png',
     'Assets/grafomotricidad/06_vaca.png',
     'Assets/grafomotricidad/07_cuadrado_med.png',
     'Assets/grafomotricidad/08_circulo_med.png',
     'Assets/grafomotricidad/09_triangulo_med.png',
     'Assets/grafomotricidad/10_perro.png',
     'Assets/grafomotricidad/11_cerdo.png',
     'Assets/grafomotricidad/12_gato.png',
     'Assets/grafomotricidad/13_cuadrado_peq.png',
     'Assets/grafomotricidad/14_circulo_peq.png',
     'Assets/grafomotricidad/15_triangulo_peq.png',
     'Assets/grafomotricidad/16_gallina.png',
     'Assets/grafomotricidad/17_caballo.png',
     'Assets/grafomotricidad/18_conejo.png',
]
     
     
# Diccionarios con el codigo de colores  para el modulo de iluminacion

ilumination_colors = {
     1: 'Rojo',
     2: 'Verde',
     3: 'Azul',
     4: 'Amarillo',
     5: 'Celeste', # cyan?
     6: 'Blanco',
     7: 'Naranja',
     8: 'Rosado', # magenta?
     9: 'Purpura'   
}

rgb_colors = {
     'Rojo':'255,0,0',
     'Verde':'0,255,0',
     'Azul':'0,0,255',
     'Amarillo':'255,255,0',
     'Celeste':'0,255,255',
     'Blanco':'255,255,255',
     'Naranja':'255,69,0',
     'Rosado':'255,0,255',
     'Purpura':'128,0,128'
}