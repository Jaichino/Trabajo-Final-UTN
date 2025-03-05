##############################################################################
# Importaciones
##############################################################################

from tkinter import *
from vista.vista_menuprincipal import VistaMenuPrincipal
from controlador.controlador_inventario import ControladorInventario
from controlador.controlador_ventas import ControladorVentas

##############################################################################
# Clase controlador del menu principal
##############################################################################

class ControladorMenuPrincipal:

    """
    En el controlador del menu principal se llevan a cabo las aperturas
    de los respectivos modulos de la aplicacion (modulo de ventas y modulo
    de inventario).

    """

    ##########################################################################
    # Constructor del controlador
    ##########################################################################

    def __init__(self,root):
        
        self.root = root
        self.vista = VistaMenuPrincipal(root)

        # Asignacion de funciones para abrir modulos a los respectivos botones
        self.vista.boton_inventario.config(
            command=self.iniciar_modulo_inventario
        )
        self.vista.boton_ventas.config(command=self.iniciar_modulo_ventas)

    ##########################################################################
    # Metodos
    ##########################################################################

    def iniciar_modulo_inventario(self):

        ''' Metodo para abrir el modulo de inventario. Se crea un TopLevel y
            se instancia el controlador del modulo de inventario. Se asigna el
            evento de cerrar modulo al TopLevel.
        '''

        self.minimizar_menu_principal()
        self.top_level = Toplevel(self.root)
        self.abrir_ventana_inventario = ControladorInventario(self.top_level)
        self.top_level.grab_set()
        self.top_level.protocol("WM_DELETE_WINDOW", self.cerrar_modulo)
    

    def iniciar_modulo_ventas(self):

        ''' Metodo para abrir el modulo de ventas. Se crea un TopLevel y
            se instancia el controlador del modulo de ventas. Se asigna el
            evento de cerrar modulo al TopLevel.
        '''
        
        self.minimizar_menu_principal()
        self.top_level = Toplevel(self.root)
        self.abrir_ventana_ventas = ControladorVentas(self.top_level)
        self.top_level.grab_set()
        self.top_level.protocol("WM_DELETE_WINDOW", self.cerrar_modulo)


    # Metodo para minimizar menu principal
    def minimizar_menu_principal(self):
        self.root.iconify()


    # Metodo para cerrar modulo y reabrir menu principal
    def cerrar_modulo(self):
        self.top_level.destroy()
        self.root.deiconify()