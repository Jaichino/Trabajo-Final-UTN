##############################################################################
# Importaciones
##############################################################################

import re

##############################################################################
# Clase validaciones de campos
##############################################################################

class Validaciones:

    ''' Clase que contiene metodos encargados de la validacion de campos
    '''

    ##########################################################################
    # Metodos
    ##########################################################################
    
    @staticmethod
    def validacion_cliente(cliente):

        ''' Metodo para realizar la validacion del campo de clientes en la
            ventana de nuevo miembro. Se verifica que el cliente ingresado
            coincida con el patron establecido.

            :param str cliente: Nombre del cliente.
            :return: Devuelve un objeto en caso de coincidir, caso contrario
                devuelve None.
        '''
        patron = r"^(?:[a-zA-Z]{3,}\s?)+$"
        coincidencia = re.match(patron, cliente)
        return coincidencia
    

    @staticmethod
    def validacion_telefono(telefono):

        ''' Metodo para realizar la validacion del campo de telefono en la
            ventana de nuevo miembro. Se verifica que el telefono ingresado
            coincida con el patron establecido.

            :param str telefono: Numero de telefono del cliente.
            :return: Devuelve un objeto en caso de coincidir, caso contrario
                devuelve None.
        '''
        
        patron = r"^\d{2,}\-\d{6,}$"
        coincidencia = re.match(patron, telefono)
        return coincidencia


    @staticmethod
    def validacion_email(email):

        ''' Metodo para realizar la validacion del campo de email en la
            ventana de nuevo miembro. Se verifica que el email ingresado
            coincida con el patron establecido.

            :param str email: Correo electronico del cliente.
            :return: Devuelve un objeto en caso de coincidir, caso contrario
                devuelve None.
        '''

        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        coincidencia = re.match(patron, email)
        return coincidencia


    @staticmethod
    def validacion_documento(documento):

        ''' Metodo para realizar la validacion del campo de documento en la
            ventana de nuevo miembro. Se verifica que el documento ingresado
            coincida con el patron establecido.

            :param int documento: Numero de documento del cliente.
            :return: Devuelve un objeto en caso de coincidir, caso contrario
                devuelve None.
        '''

        patron = r"^\d{8}$"
        coincidencia = re.match(patron, documento)
        return coincidencia