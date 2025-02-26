from tkinter import Tk, Frame, Label, Entry, Button
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from vista.configuracion_vista import ConfiguracionVista as cv

class VentanaVentas:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Market - Ventas")
        self.root.geometry(
            f"1200x600+{int((cv.res_x-1200)/2)}+{int((cv.res_y-600)/2)}"
        )
        self.root.resizable(0, 0)
        self.img = {}
        self.widgets()


    def widgets(self):
        # Referencia a imagenes
        self.img['carrito'] = cv.formato_imagen(cv.imagenes['carrito'])
        self.img['eliminar'] = cv.formato_imagen(cv.imagenes['eliminar'])
        self.img['buscar'] = cv.formato_imagen(cv.imagenes['buscar'])
        self.img['listo'] = cv.formato_imagen(cv.imagenes['listo'])

        # Frames
        self.frame_datos_venta = Frame(
            self.root,
            width=1200,
            height=150,
            background=cv.colores['background']
        )
        self.frame_datos_venta.place(x=0, y=0)

        self.frame_treeview_carrito = Frame(self.root, width=1200, height=300)
        self.frame_treeview_carrito.place(x=0, y=150)

        self.frame_finalizacion_venta = Frame(
            self.root,
            width=1200,
            height=150,
            background=cv.colores['background']
        )
        self.frame_finalizacion_venta.place(x=0, y=450)

        # Labels
        self.label_cliente = Label(
            self.frame_finalizacion_venta,
            text="Cliente",
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_cliente.place(relx=0.01, rely=0.1)

        self.label_cliente_encontrado = Label(
            self.frame_finalizacion_venta,
            text="Cliente: ",
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_cliente_encontrado.place(relx=0.01, rely=0.75)

        self.label_fecha = Label(
            self.frame_datos_venta,
            text="Fecha",
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_fecha.place(relx=0.01, rely=0.1)

        self.label_codigo = Label(
            self.frame_datos_venta,
            text="Código",
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_codigo.place(relx=0.01, rely=0.4)

        self.label_descripcion = Label(
            self.frame_datos_venta,
            text="Descripción: ",
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_descripcion.place(x=350, rely=0.1)

        self.label_cantidad = Label(
            self.frame_datos_venta,
            text="Cantidad",
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_cantidad.place(relx=0.01, rely=0.7)

        self.label_enstock = Label(
            self.frame_datos_venta,
            text="En Stock: ",
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_enstock.place(x=350, rely=0.4)

        self.label_total_venta = Label(
            self.frame_finalizacion_venta,
            text="Total de venta: $ ",
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_total_venta.place(relx=0.7, rely=0.1)

        self.label_descuentos = Label(
            self.frame_finalizacion_venta,
            text="Descuentos: $ ",
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_descuentos.place(relx=0.7, rely=0.42)

        self.label_total_a_pagar = Label(
            self.frame_finalizacion_venta,
            text="Total a pagar: $ ",
            font=cv.fuentes['texto-bold'],
            background=cv.colores['background']
        )
        self.label_total_a_pagar.place(relx=0.7, rely=0.75)

        # Entry
        self.entry_cliente = Entry(
            self.frame_finalizacion_venta,
            font=cv.fuentes['texto'],
            width=18
        )
        self.entry_cliente.place(relx=0.1, rely=0.1)

        self.entry_codigo = Entry(
            self.frame_datos_venta, font=cv.fuentes['texto'], width=15
        )
        self.entry_codigo.place(relx=0.1, rely=0.4)

        self.entry_cantidad = Entry(
            self.frame_datos_venta, font=cv.fuentes['texto'], width=15
            )
        self.entry_cantidad.place(relx=0.1, rely=0.7)

        self.entry_fecha = Entry(
            self.frame_datos_venta, font=cv.fuentes['texto'], width=15
        )
        self.entry_fecha.insert(0,date.strftime(date.today(), "%d-%m-%Y"))
        self.entry_fecha.place(relx=0.1, rely=0.1)

        # Button
        self.boton_verificar_cliente = Button(
            self.frame_finalizacion_venta,
            text='Verificar cliente',
            font=cv.fuentes['texto'],
            width=178,
            image=self.img['buscar'],
            compound='left',
            padx=10
        )
        self.boton_verificar_cliente.place(relx=0.1, rely=0.35)

        self.boton_agregar_carrito = Button(
            self.frame_datos_venta,
            text='Agregar al carrito',
            font=cv.fuentes['boton'],
            width=200,
            image=self.img['carrito'],
            compound='left',
            padx=10
        )
        self.boton_agregar_carrito.place(relx=0.38, rely=0.8, anchor='center')

        self.boton_eliminar_carrito = Button(
            self.frame_datos_venta,
            text='Eliminar del carrito',
            font=cv.fuentes['boton'],
            width=200,
            image=self.img['eliminar'],
            compound='left',
            padx=10
        )
        self.boton_eliminar_carrito.place(relx=0.6, rely=0.8, anchor='center')

        self.boton_consulta_ventas = Button(
            self.frame_datos_venta,
            text='Consultar ventas',
            font=cv.fuentes['boton'],
            width=200,
            image=self.img['buscar'],
            compound='left',
            padx=10
        )
        self.boton_consulta_ventas.place(relx=0.82, rely=0.8, anchor='center')

        self.boton_finalizar_venta = Button(
            self.frame_finalizacion_venta,
            text='Finalizar venta',
            font=cv.fuentes['boton'],
            width=200,
            image=self.img['listo'],
            compound='left',
            padx=10
        )
        self.boton_finalizar_venta.place(relx=0.5, rely=0.2, anchor='center')

        # Treeview
        self.treeview_carrito = ttk.Treeview(
            self.frame_treeview_carrito,
            columns=('col1','col2','col3','col4'),
            height=25
        )

        self.treeview_carrito.column("#0", width=150, anchor='center')
        self.treeview_carrito.column("col1", width=400, anchor='center')
        self.treeview_carrito.column("col2", width=250, anchor='center')
        self.treeview_carrito.column("col3", width=150, anchor='center')
        self.treeview_carrito.column("col4", width=250, anchor='center')

        self.treeview_carrito.heading(
            "#0", text='Codigo', anchor='center'
        )
        self.treeview_carrito.heading(
            "col1", text='Producto', anchor='center'
        )
        self.treeview_carrito.heading(
            "col2", text='Precio', anchor='center'
        )
        self.treeview_carrito.heading(
            "col3", text='Cantidad', anchor='center'
        )
        self.treeview_carrito.heading(
            "col4", text='Subtotal', anchor='center'
        )

        self.treeview_carrito.grid(row=0, column=0, sticky='nsew')

        # Style para Treeview
        self.style = ttk.Style(self.frame_treeview_carrito)
        self.style.configure(
            "Treeview.Heading",font=cv.fuentes['treeview-heading']
        )
        self.style.configure("Treeview", font=cv.fuentes['treeview'])

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(
            self.frame_treeview_carrito,
            orient='vertical',
            command=self.treeview_carrito.yview
        )
        self.treeview_carrito.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
    

    def limpiar_cajas(self):
        self.entry_cantidad.delete(0, 'end')
        self.entry_codigo.delete(0, 'end')
    
    
    def limpiar_cliente(self):
        self.entry_cliente.delete(0, 'end')
    

    def limpiar_treeview(self):
        for child in self.treeview_carrito.get_children():
            self.treeview_carrito.delete(child)


class VentanaConsultaVentas:

    def __init__(self, root):
        self.root = root
        self.root.title("Market - Consulta de ventas")
        self.root.geometry(
            f"1200x600+{int((cv.res_x-1200)/2)}+{int((cv.res_y-600)/2)}"
        )
        self.root.resizable(0, 0)
        self.img = {}
        self.widgets()


    def widgets(self):

        # Referencia a imagenes
        self.img['filtrar'] = cv.formato_imagen(cv.imagenes['filtrar'])
        self.img['eliminar'] = cv.formato_imagen(cv.imagenes['eliminar'])
        
        # Frames
        self.frame_filtro = Frame(
            self.root,
            width=1200,
            height=150,
            background=cv.colores['background']
        )
        self.frame_filtro.place(x=0, y=0)

        self.frame_treeview = Frame(self.root, width=1200, height=450)
        self.frame_treeview.place(x=2, y=150)

        # Label
        self.label_inicio = Label(
            self.frame_filtro,
            text="Desde",
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_inicio.place(relx=0.01, rely=0.2)

        self.label_final = Label(
            self.frame_filtro,
            text="Hasta",
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_final.place(relx=0.01, rely=0.6)

        # DateEntry
        self.fecha_desde = DateEntry(
            self.frame_filtro,
            date_pattern="dd-mm-yyyy",
            width=15,
            font=cv.fuentes['texto']
        )
        self.fecha_desde.place(relx=0.09, rely=0.2)

        self.fecha_hasta = DateEntry(
            self.frame_filtro,
            date_pattern="dd-mm-yyyy",
            width=15,
            font=cv.fuentes['texto']
        )
        self.fecha_hasta.place(relx=0.09, rely=0.6)

        # Button
        self.boton_filtrar = Button(
            self.frame_filtro,
            text='Filtrar',
            font=cv.fuentes['boton'],
            width=180,
            image=self.img['filtrar'],
            compound='left',
            padx=10
        )
        self.boton_filtrar.place(relx=0.36, rely=0.5, anchor='center')

        self.boton_eliminar = Button(
            self.frame_filtro,
            text='Eliminar venta',
            font=cv.fuentes['boton'],
            width=180,
            image=self.img['eliminar'],
            compound='left',
            padx=10
        )
        self.boton_eliminar.place(relx=0.55, rely=0.5, anchor='center')

        # Treeview
        self.treeview_consulta = ttk.Treeview(
            self.frame_treeview, columns=('col1','col2','col3'), height=21)
        
        self.treeview_consulta.column("#0", width=180, anchor='center')
        self.treeview_consulta.column("col1", width=300, anchor='center')
        self.treeview_consulta.column("col2", width=400, anchor='center')
        self.treeview_consulta.column("col3", width=300, anchor='center')

        self.treeview_consulta.heading("#0", text='Venta #')
        self.treeview_consulta.heading("col1", text='Fecha Venta')
        self.treeview_consulta.heading("col2", text='Cliente')
        self.treeview_consulta.heading("col3", text='Monto Venta')

        self.treeview_consulta.grid(row=0, column=0, sticky='nsew')

        self.style = ttk.Style(self.frame_treeview)
        self.style.configure(
            "Treeview.Heading", font=cv.fuentes['treeview-heading']
        )
        self.style.configure("Treeview", font=cv.fuentes['treeview'])

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(
            self.frame_treeview,
            orient='vertical',
            command=self.treeview_consulta.yview
        )
        self.treeview_consulta.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
    

    def limpiar_treeview(self):
        for child in self.treeview_consulta.get_children():
            self.treeview_consulta.delete(child)


class VentanaMiembros:

    # Constructor de la ventana de ingreso de nuevos miembros
    def __init__(self,root):
        self.root = root
        self.root.title("Market - Registro nuevo miembro")
        self.root.geometry(
            f"400x350+{int((cv.res_x-400)/2)}+{int((cv.res_y-350)/2)}"
        )
        self.root.resizable(0, 0)
        self.img = {}
        self.root.config(bg=cv.colores['background'])
        self.widgets()
    

    def widgets(self):
        # Referencia a imagenes
        self.img['listo'] = cv.formato_imagen(cv.imagenes['listo'])

        # Label
        self.label_cliente = Label(
            self.root,
            text='Cliente',
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_cliente.place(relx=0.05, rely=0.05)

        self.label_documento = Label(
            self.root,
            text='DNI',
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_documento.place(relx=0.05, rely=0.25)

        self.label_telefono = Label(
            self.root,
            text='Teléfono',
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_telefono.place(relx=0.05, rely=0.45)

        self.label_email = Label(
            self.root,
            text='Email',
            font=cv.fuentes['texto'],
            background=cv.colores['background']
        )
        self.label_email.place(relx=0.05, rely=0.65)

        # Entry
        self.entry_cliente = Entry(
            self.root, font=cv.fuentes['texto'], width=20
        )
        self.entry_cliente.place(relx=0.35, rely=0.05)

        self.entry_documento = Entry(
            self.root, font=cv.fuentes['texto'], width=20
        )
        self.entry_documento.place(relx=0.35, rely=0.25)

        self.entry_telefono = Entry(
            self.root, font=cv.fuentes['texto'], width=20
        )
        self.entry_telefono.place(relx=0.35, rely=0.45)

        self.entry_email = Entry(
            self.root, font=cv.fuentes['texto'], width=20
        )
        self.entry_email.place(relx=0.35, rely=0.65)

        # Button
        self.boton_guardar = Button(
            self.root, 
            text='Registrar', 
            font=cv.fuentes['boton'], 
            width=150,
            image=self.img['listo'],
            compound='left',
            padx=10
        )
        self.boton_guardar.place(relx=0.5, rely=0.88, anchor='center')
    

    def limpiar_cajas(self):
        self.entry_cliente.delete(0, 'end')
        self.entry_documento.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_telefono.delete(0, 'end')