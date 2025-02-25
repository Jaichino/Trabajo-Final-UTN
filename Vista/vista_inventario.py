from tkinter import Tk, Label, Button, Frame, Entry
from tkinter import ttk
from vista.configuracion_vista import ConfiguracionVista as cv

class VentanaInventario:

    def __init__(self, root):
        self.root = root
        self.root.title("Market - Inventario")
        self.root.geometry(
            f"1200x600+{int((cv.res_x-1200)/2)}+{int((cv.res_y-600)/2)}"
        )
        self.root.resizable(0, 0)
        self.widgets()


    def widgets(self):
        
        # Frame del Treeview
        self.frame_treeview = Frame(self.root, width=800, height=600)
        self.frame_treeview.place(x=1, y=0)

        # Frame de funcionalidades
        self.frame_funcionalidades = Frame(
            self.root, width=400, height=600, bg=cv.colores['background']
        )
        self.frame_funcionalidades.place(x=800, y=0)

        # Frame línea divisora funcionalidades
        self.frame_linea = Frame(
            self.frame_funcionalidades,
            width=400, 
            height=3,
            bg=cv.colores['divisor']
        )
        
        self.frame_linea.place(x=0, y=300)

        # Titulo frame funcionalidades
        self.label_funcionalidades = Label(
            self.frame_funcionalidades,
            text="BÚSQUEDA",
            font=cv.fuentes['titulo'],
            bg=cv.colores['background']
        )
        self.label_funcionalidades.place(
            relx=0.5, rely=0.05, anchor='center'
        )

        # Entry, Label y Button de búsqueda
        self.label_codigo = Label(
            self.frame_funcionalidades,
            text="Código", 
            font=cv.fuentes['texto'], 
            bg=cv.colores['background']
        )
        self.label_codigo.place(relx=0.05, rely=0.12)
        self.label_descripcion = Label(
            self.frame_funcionalidades,
            text="Descripción", 
            font=cv.fuentes['texto'], 
            bg=cv.colores['background']
        )
        self.label_descripcion.place(relx=0.05, rely=0.22)

        self.entry_codigo = Entry(
            self.frame_funcionalidades,
            font=cv.fuentes['texto'], 
            width=19
        )
        
        self.entry_codigo.place(relx=0.4, rely=0.12)
        self.entry_descripcion = Entry(
            self.frame_funcionalidades, font=cv.fuentes['texto'], width=19
        )
        self.entry_descripcion.place(relx=0.4, rely=0.22)

        self.boton_buscar = Button(
            self.frame_funcionalidades, 
            text="Filtrar", 
            width=10, 
            font=cv.fuentes['boton']
        )
        self.boton_buscar.place(relx=0.5, rely=0.36,anchor='center')

        self.boton_sin_stock = Button(
            self.frame_funcionalidades, 
            text="Sin Stock", 
            width=10, 
            font=cv.fuentes['boton']
        )
        self.boton_sin_stock.place(relx=0.5, rely=0.45, anchor='center')

        # Botones nuevo producto, editar producto y eliminar producto
        self.boton_nuevo_producto = Button(
            self.frame_funcionalidades, 
            text="Nuevo Producto", 
            width=20, 
            font=cv.fuentes['boton']
        )
        self.boton_nuevo_producto.place(relx=0.5, rely=0.6,anchor='center')
        self.boton_editar_producto = Button(
            self.frame_funcionalidades, 
            text="Editar Producto", 
            width=20, 
            font=cv.fuentes['boton']
        )
        self.boton_editar_producto.place(
            relx=0.5, rely=0.75, anchor='center'
        )
        self.boton_eliminar_producto = Button(
            self.frame_funcionalidades, 
            text="Eliminar Producto", 
            width=20, 
            font=cv.fuentes['boton']
        )
        self.boton_eliminar_producto.place(
            relx=0.5, rely=0.9, anchor='center'
        )

        # Treeview inventario
        self.treeview_inventario = ttk.Treeview(
            self.frame_treeview,
            columns=('col1','col2','col3'),
            height=28
        )
        
        self.treeview_inventario.column("#0", width=80, anchor='center')
        self.treeview_inventario.column("col1", width=400, anchor='center')
        self.treeview_inventario.column("col2", width=150, anchor='center')
        self.treeview_inventario.column("col3", width=150, anchor='center')
        
        self.treeview_inventario.heading(
            "#0", text="Código", anchor='center'
        )
        self.treeview_inventario.heading(
            "col1", text="Descripción", anchor='center'
        )
        self.treeview_inventario.heading(
            "col2", text="Precio Unitario", anchor='center'
        )
        self.treeview_inventario.heading(
            "col3", text="Cantidad", anchor='center'
        )

        self.style = ttk.Style(self.frame_treeview)
        self.style.configure(
            "Treeview.Heading",
            font=cv.fuentes['treeview-heading']
        )
        self.style.configure("Treeview", font=cv.fuentes['treeview'])

        self.treeview_inventario.grid(row=0, column=0, sticky='nswe')

        # Scrollbar treeview
        self.scrollbar = ttk.Scrollbar(
            self.frame_treeview,
            orient='vertical',
            command=self.treeview_inventario.yview
        )
        self.treeview_inventario.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')


    def limpiar_cajas(self):
        self.entry_descripcion.delete(0, 'end')
        self.entry_codigo.delete(0, 'end')
    

    def limpiar_treeview(self):
        for child in self.treeview_inventario.get_children():
            self.treeview_inventario.delete(child)

class VentanaDetalleProducto:

    # Constructor de la ventana Detalle de Producto
    def __init__(self,root):
        self.root = root
        self.root.title("Inventario - Ventana de Producto")
        self.root.geometry(
            f"400x350+{int((cv.res_x-400)/2)}+{int((cv.res_y-350)/2)}"
        )
        self.root.resizable(0, 0)
        self.root.config(bg=cv.colores['background'])
        self.widgets()
    
    
    # Widgets de la ventana
    def widgets(self):
        
        # Label
        self.label_descripcion = Label(
            self.root,
            text='Descripción',
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_descripcion.place(relx=0.05, rely=0.15)

        self.label_precio = Label(
            self.root,
            text='Precio',
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_precio.place(relx=0.05, rely=0.35)

        self.label_cantidad = Label(
            self.root,
            text='Cantidad',
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_cantidad.place(relx=0.05, rely=0.55)

        # Entry
        self.entry_descripcion = Entry(
            self.root, font=cv.fuentes['texto'],width=20
        )
        self.entry_descripcion.place(relx=0.35, rely=0.15)

        self.entry_precio = Entry(
            self.root, font=cv.fuentes['texto'], width=20
        )
        self.entry_precio.place(relx=0.35, rely=0.35)

        self.entry_cantidad = Entry(
            self.root, font=cv.fuentes['texto'], width=20
        )
        self.entry_cantidad.place(relx=0.35, rely=0.55)

        # Button
        self.boton_guardar = Button(
            self.root, text='Guardar', font=cv.fuentes['boton'], width=15
        )
        self.boton_guardar.place(relx=0.5, rely=0.85, anchor='center')
    

    def limpiar_cajas(self):
        self.entry_cantidad.delete(0, 'end')
        self.entry_descripcion.delete(0, 'end')
        self.entry_precio.delete(0, 'end')