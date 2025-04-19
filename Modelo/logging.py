##############################################################################
# Importaciones
##############################################################################

from datetime import datetime
import functools

##############################################################################
# Creacion decorador de logging
##############################################################################

def registro_logging(mensaje="Accion ejecutada"):
    
    ''' Funcion decoradora utilizada para generar un registro de logging
        tanto en pantalla como en un archivo .txt para llevar registro
        de las acciones realizadas en el sistema.

        :return: Funcion decorada con registro de log
    '''
    
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Se calcula fecha y hora actual 
            tiempo_accion = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            
            # Configuracion de mensaje de log
            linea_log = f"[{tiempo_accion}] INFO: {mensaje}"

            # Se agregan args/kwargs a linea de log
            if args:
                linea_log += f" - Args: {args}"
            if kwargs:
                linea_log += f" - Kwargs: {kwargs}"

            # Se muestra accion en pantalla
            print(linea_log)

            # Registro en txt
            with open("control_logging.txt", "a") as archivo:
                archivo.write(linea_log + "\n")
            
            return func(*args, **kwargs)
        return wrapper
    return decorador