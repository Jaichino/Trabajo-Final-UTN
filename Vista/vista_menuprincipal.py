from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk
from vista.configuracion_vista import ConfiguracionVista as cv


class VistaMenuPrincipal:

    def __init__(self, root):
        self.root = root
        self.root.title("Market - Menú Principal")
        self.root.geometry(f"500x500+{int((cv.res_x-500)/2)}+{int((cv.res_y-500)/2)}")
        self.root.resizable(0, 0)
        self.widgets()


    def widgets(self):
        # Frame del logo
        self.frame_logo = Frame(self.root, width=500, height=300,bg=cv.colores['background'])
        self.frame_logo.place(x=0, y=0)

        # Frame de los botones
        self.frame_botones = Frame(self.root, width=500, height=200,bg=cv.colores['background'])
        self.frame_botones.place(x=0, y=300)

        # Botones
        self.boton_inventario = Button(self.frame_botones, text="INVENTARIO", width=25,height=2, font=cv.fuentes['boton'])
        self.boton_inventario.place(relx=0.5, rely=0.2, anchor='center')

        self.boton_ventas = Button(self.frame_botones, text="VENTAS", width=25,height=2, font=cv.fuentes['boton'])
        self.boton_ventas.place(relx=0.5, rely=0.6, anchor='center')

        # Logo del negocio
        imagen_pil = Image.open('logo.png')
        imagen_pil_resize = imagen_pil.resize((250,250))
        imagen_tk = ImageTk.PhotoImage(imagen_pil_resize)
        self.label_logo = Label(self.frame_logo,width=500,height=300,image=imagen_tk,background=cv.colores['background'])
        self.label_logo.pack()
        self.label_logo.image = imagen_tk

