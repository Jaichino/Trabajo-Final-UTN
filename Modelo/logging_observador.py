##############################################################################
# Importaciones
##############################################################################

from datetime import datetime

###############################################################################
# Desarrollo patrón observador para control de logging
###############################################################################

# CLASE BASE OBSERVER

class Observer:
    def update(self, mensaje: str):
        raise NotImplementedError("El observador debe implementar el método 'update'.")


# SUBJECT

class Subject:
    def __init__(self):
        self._observadores = []
    

    def agregar(self, observador: Observer):
        self._observadores.append(observador)
    

    def notificar(self, mensaje: str):
        for observador in self._observadores:
            observador.update(mensaje)

# OBSERVADORES

class LoggerConsola(Observer):
    def update(self, mensaje: str):
        print(f"[CONSOLA OBSERVADOR] {mensaje}")


class LoggerArchivo(Observer):
    def __init__(self, ruta_archivo="control_logging.txt"):
        self.ruta = ruta_archivo

    
    def update(self, mensaje: str):
        with open(self.ruta, "a") as f:
            f.write(f"[CONSOLA OBSERVADOR] {mensaje}\n")


# CLASE LOGGER PRINCIPAL

class LoggerSistema(Subject):
    def log(self, mensaje: str, args=None, kwargs=None):
        hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        linea = f"[{hora}] INFO: {mensaje}"
        if args:
            linea += f" - Args: {args}"
        
        if kwargs:
            linea += f" - Kwargs: '{kwargs}"
        
        self.notificar(linea)


# INSTANCIA DE LOGGER

logger = LoggerSistema()
logger.agregar(LoggerConsola())
logger.agregar(LoggerArchivo())