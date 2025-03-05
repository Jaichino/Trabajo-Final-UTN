##############################################################################
# Importaciones
##############################################################################

from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk
from vista.configuracion_vista import ConfiguracionVista as cv

##############################################################################
# Ventana Menu Principal
##############################################################################

class VistaMenuPrincipal:

    ''' Clase donde se genera la interfaz grafica para del menu principal de
        la aplicacion.
    '''
    
    ##########################################################################    
    # Constructor de la ventana
    ##########################################################################
    
    def __init__(self, root):
        self.root = root
        self.root.title("Market - Menú Principal")
        self.root.geometry(
            f"500x500+{int((cv.res_x-500)/2)}+{int((cv.res_y-500)/2)}"
        )
        self.root.resizable(0, 0)
        self.root.iconbitmap('logo.ico')
        self.imagenes = {}
        self.widgets()


    def widgets(self):
        
        ######################################################################
        # Referencia a imagenes
        ######################################################################
        
        self.imagenes['ventas'] = cv.formato_imagen(
            cv.imagenes['ventas'],
            'menu'
        )
        self.imagenes['inventario'] = cv.formato_imagen(
            cv.imagenes['inventario'],
            'menu'
        )

        ######################################################################
        # Frames
        ######################################################################
        
        self.frame_logo = Frame(
            self.root, width=500, height=300, bg=cv.colores['background']
        )
        self.frame_logo.place(x=0, y=0)

        self.frame_botones = Frame(
            self.root, width=500, height=200, bg=cv.colores['background']
        )
        self.frame_botones.place(x=0, y=300)

        ######################################################################
        # Buttons
        ######################################################################
        
        self.boton_inventario = Button(
            self.frame_botones, 
            text="INVENTARIO", 
            width=200,
            compound='left',
            border=2,
            relief='solid',
            font=cv.fuentes['boton'],
            image=self.imagenes['inventario'],
            padx=20
        )
        self.boton_inventario.place(relx=0.5, rely=0.25, anchor='center')

        self.boton_ventas = Button(
            self.frame_botones, 
            text="VENTAS", 
            width=200,
            border=2,
            relief='solid',
            font=cv.fuentes['boton'],
            image=self.imagenes['ventas'],
            compound='left',
            padx=20
        )
        self.boton_ventas.place(relx=0.5, rely=0.65, anchor='center')

        ######################################################################
        # Logo negocio
        ######################################################################
        
        imagen_pil = Image.open('logo.png')
        imagen_pil_resize = imagen_pil.resize((250, 250))
        imagen_tk = ImageTk.PhotoImage(imagen_pil_resize)
        self.label_logo = Label(
            self.frame_logo,
            width=500,
            height=300,
            image=imagen_tk,
            background=cv.colores['background']
        )
        self.label_logo.pack()
        self.label_logo.image = imagen_tk

