import re

class Validaciones:
    
    @staticmethod
    def validacion_cliente(cliente):
        patron = r"^(?:[a-zA-Z]{3,}\s?)+$"
        coincidencia = re.match(patron, cliente)
        return coincidencia
    

    @staticmethod
    def validacion_telefono(telefono):
        patron = r"^\d{2,}\-\d{6,}$"
        coincidencia = re.match(patron, telefono)
        return coincidencia
    

    @staticmethod
    def validacion_email(email):
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        coincidencia = re.match(patron, email)
        return coincidencia
    
    
    @staticmethod
    def validacion_documento(documento):
        patron = r"^\d{8}$"
        coincidencia = re.match(patron, documento)
        return coincidencia