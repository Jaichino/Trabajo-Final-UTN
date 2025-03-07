##############################################################################
# Importaciones
##############################################################################

from tkinter import *
from tkinter import messagebox
from modelo.modelo_inventario import ModeloInventario
from vista.vista_inventario import VentanaInventario, VentanaDetalleProducto

##############################################################################
# Clase Controlador Inventario
##############################################################################

class ControladorInventario:

    ''' La clase ControladorInventario es la encargada de la comunicacion de
        la logica del negocio con la interfaz grafica del modulo Inventario.
    '''

    ##########################################################################
    # Constructor del controlador
    ##########################################################################

    def __init__(self,root):

        self.root = root
        self.vista_inventario = VentanaInventario(self.root)
        self.modelo_inventario = ModeloInventario()

        # Focus en campo de codigo al iniciarse la ventana
        self.vista_inventario.entry_codigo.focus()

        # Inicializacion del Treeview con productos
        self.llenar_treeview_productos()
        
        # Se guarda la seleccion del treeview
        self.seleccion = ()

        # Se guarda id_producto segun self.seleccion
        self.id_producto = None

        # Configuracion boton nuevo producto
        self.vista_inventario.boton_nuevo_producto.config(
            command = self.abrir_nuevo_producto
        )

        # Configuracion boton modificar producto
        self.vista_inventario.boton_editar_producto.config(
            command = self.abrir_modificacion_producto
        )

        # Configuracion boton filtrado de productos
        self.vista_inventario.boton_buscar.config(
            command = self.boton_filtrar_productos
        )

        # Configuracion boton productos sin stock
        self.vista_inventario.boton_sin_stock.config(
            command = self.boton_sin_stock
        )

        # Configuracion boton eliminar producto
        self.vista_inventario.boton_eliminar_producto.config(
            command = self.boton_eliminar_producto
        )

    ##########################################################################
    # Metodos 
    ##########################################################################

    def llenar_treeview_productos(self):

        ''' Metodo para llenar el treeview con productos existentes en la base
            de datos. Se buscan los productos utilizando 'mostrar_productos',
            luego, si existen resultados, se insertan en treeview.
        '''
        # Obtencion de lista de productos
        productos = self.modelo_inventario.mostrar_productos()

        # Limpieza de treeview
        self.vista_inventario.limpiar_treeview()

        # Si se encuentran productos, se itera lista y se agregan a treeview
        if productos:
            for prod in productos:
                self.vista_inventario.treeview_inventario.insert(
                    '',
                    'end',
                    text = prod[0],
                    values = (prod[1], prod[2], prod[3])
                )


    def abrir_nuevo_producto(self):
        
        ''' Metodo para permitir la apertura de la ventana de detalle de
            producto mediante el 'boton_nuevo_producto' unicamente si no
            se han elegido productos en el treeview.
        '''

        self.seleccion = self.vista_inventario.treeview_inventario.selection()
        if self.seleccion:
            messagebox.showwarning(
                'Error',
                'No debes seleccionar elementos'
            )
        else:
            self.ventana_detalle_producto()


    def abrir_modificacion_producto(self):

        ''' Metodo para permitir la apertura de la ventana de detalle de
            producto mediante el 'boton_nuevo_producto' unicamente si se 
            ha elegido un unico producto en el treeview.
        '''

        self.seleccion = self.vista_inventario.treeview_inventario.selection()
        if len(self.seleccion) > 1:
            messagebox.showwarning(
                'Error',
                'Debes seleccionar solo un elemento'
            )
            return

        elif self.seleccion:
            self.ventana_detalle_producto()
        
        else:
            messagebox.showwarning(
                'Error',
                'Debes seleccionar un elemento'
            )


    def ventana_detalle_producto(self):

        ''' Metodo encargado de la creacion de un TopLevel para la apertura
            de la ventana de detalle de producto. En caso de que se haya
            seleccionado un elemento del treeview, se iniciara la ventana
            con los Entry 'entry_descripcion', 'entry_precio' y
            'entry_cantidad' con la informacion correspondiente al elemento
            seleccionado.
            La informacion del producto se extrae mediante el metodo llamado
            'info_producto'.
        '''

        self.top_level = Toplevel(self.root)
        self.abrir_detalle_producto = VentanaDetalleProducto(self.top_level)
        self.top_level.grab_set()
        
        self.seleccion = self.vista_inventario.treeview_inventario.selection()
        if self.seleccion:
            #Se obtiene y se guarda id de producto
            self.id_producto = self.vista_inventario.treeview_inventario.item(
                self.seleccion,
                'text'
            )
            # Inicializacion de ventana con entries llenos
            info_producto = self.modelo_inventario.info_producto(
                self.id_producto
            )

            self.abrir_detalle_producto.entry_descripcion.insert(
                0,info_producto[0][0]
            )
            self.abrir_detalle_producto.entry_precio.insert(
                0,info_producto[0][1]
            )
            self.abrir_detalle_producto.entry_cantidad.insert(
                0,info_producto[0][2]
            )
        
        self.abrir_detalle_producto.boton_guardar.config(
            command = self.boton_guardar_producto
        )


    def boton_filtrar_productos(self):
        
        ''' Metodo para realizar el filtrado de productos en treeview.
            Se obtiene valor de 'codigo' y 'descripcion' para luego llamar el
            metodo 'filtrar_productos'. Si se obtienen resultados, se llena
            treeview.
        '''

        # Obtencion de entradas de usuario
        codigo = self.vista_inventario.entry_codigo.get()
        descripcion = self.vista_inventario.entry_descripcion.get()
        codigo = None if codigo == '' else codigo
        descripcion = None if descripcion == '' else descripcion

        # Limpieza de Treeview
        self.vista_inventario.limpiar_treeview()

        # Llamado a la funcion filtro de productos
        productos_filtrados = self.modelo_inventario.filtrar_productos(
            codigo,
            descripcion
        )

        # Llenado de treeview
        if productos_filtrados:
            for prod in productos_filtrados:
                self.vista_inventario.treeview_inventario.insert(
                    '',
                    'end',
                    text = prod[0],
                    values = (prod[1], prod[2], prod[3])
                )
        
        # Limpieza de cajas y focus en entry codigo
        self.vista_inventario.limpiar_cajas()
        self.vista_inventario.entry_codigo.focus()


    def boton_sin_stock(self):

        ''' Metodo para el filtrado de productos sin stock. Se usa el metodo
            'productos_sin_stock' para obtener aquellos productos con stock
            igual a cero. En caso de obtenerse resultados, se llena el
            treeview con dichos productos, caso contrario se muestra un
            mensaje diciendo que no hay productos sin stock.
        '''

        # Limpieza de treview
        self.vista_inventario.limpiar_treeview()
    
        # Llamado de funcion filtrar productos sin stock y llenado de treeview
        sin_stock = self.modelo_inventario.productos_sin_stock()
        if sin_stock:
            for prod in sin_stock:
                self.vista_inventario.treeview_inventario.insert(
                    '',
                    'end',
                    text = prod[0],
                    values = (prod[1], prod[2], prod[3])
                )
        else:
            # Mensaje de aviso y se llena treeview con todos los productos
            messagebox.showinfo(
                'Productos',
                'No se encontraron productos sin stock'
            )
            self.llenar_treeview_productos()


    def boton_guardar_producto(self):

        ''' Metodo para guardar cambios en un producto. Se utiliza para
            crear nuevos productos (en caso de no haber seleccionado 
            ningun elemento del treeview) o para modificar un producto
            existente (previa seleccion del elemento en treeview).
            Se obtienen las entradas de usuario para los campos de 
            'descripcion', 'precio' y 'cantidad' y luego se llama a los 
            metodos 'nuevo_producto' o 'modificar_producto'.

            :raises ValueError: Si se presenta error en tipo de datos.
        '''

        try:
            # Se recuperan valores de entry
            descripcion = self.abrir_detalle_producto.entry_descripcion.get()
            precio = float(self.abrir_detalle_producto.entry_precio.get())
            cantidad = int(self.abrir_detalle_producto.entry_cantidad.get())

            # Se verifica que los campos esten completos
            if descripcion == '' or precio == '' or cantidad == '':
                messagebox.showerror(
                    'Error',
                    'Completar todos los campos'
                )
                return

            # Si self.seleccion = 0, nuevo producto, caso contrario, modificar
            if not self.seleccion:
                self.modelo_inventario.nuevo_producto(
                    descripcion,precio,cantidad
                )
            else:
                self.modelo_inventario.modificar_producto(
                    descripcion, precio, cantidad, self.id_producto
                )
        
            # Se cierra la ventana y se actualiza el treeview
            self.top_level.destroy()
            self.vista_inventario.limpiar_treeview()
            self.llenar_treeview_productos()
            
            # Se muestra mensaje de confirmacion
            if self.seleccion:
                messagebox.showinfo(
                    'Producto Modificado',
                    f'Producto ({descripcion}) modificado correctamente'
                )
            else:
                messagebox.showinfo(
                    'Nuevo producto',
                    f'Producto ({descripcion}) creado correctamente'
                )
        
        # Manejo de excepciones
        except ValueError:
            messagebox.showerror('Error','Error en tipo de datos')


    def boton_eliminar_producto(self):

        ''' Metodo para realizar la eliminacion de productos de la base de
            datos. Se verifica la seleccion de producto en treeview y se
            llama al metodo 'eliminar_producto' siendo el parametro el
            'id_producto' obtenido del treeview segun el elemento
            seleccionado.
        '''

        # Verificacion seleccion de elementos
        self.seleccion = self.vista_inventario.treeview_inventario.selection()
        if len(self.seleccion) != 1:
            messagebox.showwarning(
                'Error',
                'Debes seleccionar UN elemento'
            )
            return

        # Obtencion id_producto
        self.id_producto = self.vista_inventario.treeview_inventario.item(
            self.seleccion,
            'text'
        )
    
        # Consulta de eliminacion
        confirmacion = messagebox.askyesno(
            'Confirmacion',
            f'¿Desea eliminar el producto ({self.id_producto})?'
        )
        # Eliminacion, actualizacion de treeview y mensaje de confirmacion
        if confirmacion:
            self.modelo_inventario.eliminar_producto(self.id_producto)
            # Mensaje de confirmacion y actualizacion de treeview
            self.vista_inventario.limpiar_treeview()
            self.llenar_treeview_productos()
            messagebox.showinfo(
                'Producto eliminado',
                f'Producto ({self.id_producto}) eliminado del stock!'
            )
