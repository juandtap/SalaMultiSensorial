import sys
sys.path.append(".")

from Model.model import session, Sesion
# Sesion es la clase
# session es la sesion de la conexion con la base de datos


# Create Sesion

def add_sesion_module(new_sesion):
    flag = 0
    try:
        session.add(new_sesion)
        session.commit()
        flag = new_sesion.id
    except Exception as ex:
        session.rollback()  
        print("Error ", ex)  
    finally:
        session.close()
    return flag


# Create ModuloGrafomotricidad

def add_module_grafomotricidad(new_module):
    flag = False
    try:
        session.add(new_module)
        session.commit()
        flag = True
    except Exception as ex:
        session.rollback()
        print("Error ", ex)
    finally:
        session.close()
    
    return flag
    
# Read

def get_sesion_by_id(id_sesion):
    return session.query(Sesion).filter_by(id=id_sesion).first()

# Update
 # este metodo se ejecuta al cerrar la ventana seleccion de modulos
 # agrega la hora_fin a la sesion
 
def set_final_time(id_sesion, final_time):
    try:
        sesion_to_update = get_sesion_by_id(id_sesion)
        sesion_to_update.hora_fin = final_time
        session.commit()
    except Exception as ex:
        print(f"Error al actualizar hora_fin de sesion con id {id_sesion}: {str(ex)}")
        session.rollback()
    finally:
        session.close()

     
     