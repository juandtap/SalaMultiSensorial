# diccionario con las direcciones MAC de los modulos HC05

module_mac_address = {
     0:'00:22:03:01:8A:12', # HC05 de prueba
     1:'00:22:03:01:7D:DC', # HC05 del modulo grafomotricidad
     2:'00:22:03:01:8D:B5', # HC05 del vumetro   
     3:'00:22:03:01:7C:D5', # HC05 de iluminacion
     4:'98:D3:31:F9:42:92',  #  raspberry
}
# para pruebas, comentar a la hora de probar con los modulos
# module_mac_address = {
#      0:'00:22:03:01:8A:12',  
#      1:'00:22:03:01:8A:12', 
#      2:'00:22:03:01:8A:12', 
#      3:'00:22:03:01:8A:12', 
#      #4:'B8:27:EB:94:95:C8',
#      4:'E4:5F:01:40:62:EF'
# }



# diccionario figuras del modulo
# se tiene dos ya que el modulo de grafomotricidad se tiene un orden distinto

codigo_figuras_recibidos = {
     1: 'Vaca',
     2: 'Oveja',
     3: 'Triángulo grande',
     4: 'Cuadrado grande',
     5: 'Cerdo',
     6: 'Perro',
     7: 'Triángulo mediano',
     8: 'Círculo mediano',
     9: 'Cuadrado mediano',
     10: 'Caballo',
     11: 'Triángulo pequeño',
     12: 'Círculo pequeño',
     13: 'Cuadrado pequeño',
     14: 'Tortuga',
     15: 'Círculo grande',
     16: 'Gato',
     17: 'Conejo',
     18: 'Gallina',
}


codigo_figuras = {
     
     1: 'Cuadrado grande',
     2: 'Circulo grande',
     3: 'Triángulo grande',
     4: 'Tortuga',
     5: 'Oveja',
     6: 'Vaca',
     7: 'Cuadrado mediano',
     8: 'Círculo mediano',
     9: 'Triángulo mediano',
     10: 'Perro',
     11: 'Cerdo',
     12: 'Gato',
     13: 'Cuadrado pequeño',
     14: 'Círculo pequeño ',
     15: 'Triángulo pequeño',
     16: 'Gallina',
     17: 'Caballo',
     18: 'Conejo',
     
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
     'Rojo':'255,000,000',
     'Verde':'000,255,000',
     'Azul':'000,000,255',
     'Amarillo':'255,255,000',
     'Celeste':'000,255,255',
     'Blanco':'255,255,255',
     'Naranja':'255,069,000',
     'Rosado':'255,000,255',
     'Purpura':'128,000,128'
}