##############################################################################
# Importaciones
##############################################################################

from tkinter import Tk
from controlador.controlador_menuprincipal import ControladorMenuPrincipal

##############################################################################
# Función iniciadora de sistema
##############################################################################

def main():

    ''' El main del programa, es el encargado de iniciar la aplicacion
        llamando al controlador del menu principal, a partir del cual
        se desencadenaran las demas ventanas y controladores.
    '''

    root = Tk()
    ControladorMenuPrincipal(root)
    root.mainloop()


if __name__ == '__main__':
    main()
