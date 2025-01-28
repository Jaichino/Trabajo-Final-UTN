from tkinter import Toplevel
from Vista.vista_menuprincipal import VistaMenuPrincipal
from Vista.vista_inventario import VentanaInventario, VentanaDetalleProducto
from Vista.vista_ventas import VentanaVentas, VentanaConsultaVentas, VentanaMiembros

class ControladorMenuPrincipal:

    """
    En el controlador del menu principal se llevan a cabo las aperturas
    de los respectivos modulos de la aplicacion (modulo de ventas y modulo
    de inventario).
    """

    def __init__(self,root):
        self.root = root
        self.vista = VistaMenuPrincipal(root)

        # Asignacion de funciones para abrir modulos a los respectivos botones
        self.vista.boton_inventario.config(command=self.iniciar_modulo_inventario)
        self.vista.boton_ventas.config(command=self.iniciar_modulo_ventas)

    """
    Metodos para iniciar los modulos de inventario y ventas, primero se minimiza el
    menu principal utilizando el metodo iconify(), se genera un TopLevel de root y 
    se instancian las clases para generar las vistas correspondientes. Se establece 
    protocolo en TopLevel para cerrar modulos al cerrar la ventana desde la cruz, 
    esto llama nuevamente al menu principal.
    """

    def iniciar_modulo_inventario(self):
        self.minimizar_menu_principal()
        self.top_level = Toplevel(self.root)
        self.abrir_ventana_inventario = VentanaInventario(self.top_level)
        self.top_level.grab_set()
        self.top_level.protocol("WM_DELETE_WINDOW",self.cerrar_modulo)
    

    def iniciar_modulo_ventas(self):
        self.minimizar_menu_principal()
        self.top_level = Toplevel(self.root)
        self.abrir_ventana_ventas = VentanaVentas(self.top_level)
        self.top_level.grab_set()
        self.top_level.protocol("WM_DELETE_WINDOW",self.cerrar_modulo)

    
    # Método para minimizar menu principal
    def minimizar_menu_principal(self):
        self.root.iconify()


    # Método para cerrar modulo y reabrir menu principal
    def cerrar_modulo(self):
        self.top_level.destroy()
        self.root.deiconify()