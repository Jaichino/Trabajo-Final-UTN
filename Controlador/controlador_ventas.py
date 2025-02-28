##############################################################################
# Importaciones
##############################################################################

from tkinter import *
from tkinter import messagebox
from modelo.modelo_ventas import ModeloVentas
from modelo.modelo_inventario import ModeloInventario
from vista.vista_ventas import (
    VentanaVentas, 
    VentanaConsultaVentas, 
    VentanaMiembros, 
    VentanaConfiguracionDescuentos
)
from modelo.validacion import Validaciones

##############################################################################
# Clase controlador de ventas
##############################################################################

class ControladorVentas:
    
    ##########################################################################
    # Constructor del controlador
    ##########################################################################

    def __init__(self,root):

        # Inicializacion de ventana y modelo
        self.root = root
        self.vista_ventas = VentanaVentas(self.root)
        self.modelo_ventas = ModeloVentas()

        # Inicio de ventana con cursor en entry_codigo
        self.vista_ventas.entry_codigo.focus()

        # Guardado valor totales de venta
        self.total_venta = 0
        self.total_pagar = 0

        # Guardado id_cliente
        self.cliente = 0

        # Seteo descuento_aplicado
        self.descuento_aplicado = 0

        # Asignacion de evento a entry_codigo
        self.vista_ventas.entry_codigo.bind(
            "<KeyRelease>", 
            self.completar_detalle_producto
            )
        
        # Asignacion de metodo agregar a carrito
        self.vista_ventas.boton_agregar_carrito.config(
            command = self.boton_agregar_carrito
        )

        # Asignacion de metodo eliminar carrito
        self.vista_ventas.boton_eliminar_carrito.config(
            command = self.boton_eliminar_carrito
        )

        # Asignacion de metodo finalizar venta
        self.vista_ventas.boton_finalizar_venta.config(
            command = self.boton_finalizar_venta
        )

        # Asignacion de metodo a boton validar cliente
        self.vista_ventas.boton_verificar_cliente.config(
            command = self.boton_verificar_cliente
        )

        # Asignacion metodo apertura ventana consulta de ventas
        self.vista_ventas.boton_consulta_ventas.config(
            command = self.ventana_consulta_ventas
        )

        # Asignacion metodo apertura ventana configuraciones
        self.vista_ventas.boton_configuracion.config(
            command = self.ventana_configuracion
        )
    
    ##########################################################################
    # Metodos
    ##########################################################################

    def ventana_configuracion(self):
        # Generacion de TopLevel para apertura de ventana
        self.top_level = Toplevel(self.root)
        self.abrir_configuracion = VentanaConfiguracionDescuentos(
            self.top_level
        )
        self.top_level.grab_set()

        # Iniciacion de entries con valores actuales de descuento y monto
        self.abrir_configuracion.entry_descuento.insert(
            0,
            self.modelo_ventas.descuento()[0][0]
        )

        self.abrir_configuracion.entry_monto.insert(
            0,
            self.modelo_ventas.monto_minimo()[0][0]
        )

        # Asignacion de metodo a boton guardado de descuento
        self.abrir_configuracion.boton_guardar.config(
            command = self.actualizar_descuento_monto
        )

    
    def ventana_consulta_ventas(self):
        # Generacion de TopLevel para apertura de ventana
        self.top_level = Toplevel(self.root)
        self.abrir_consulta_ventas = VentanaConsultaVentas(self.top_level)
        self.top_level.grab_set()

        # Asignacion de metodo para filtrado de ventas
        self.abrir_consulta_ventas.boton_filtrar.config(
            command = self.filtrado_consulta_ventas
        )

        # Asignacion metodo eliminacion de ventas
        self.abrir_consulta_ventas.boton_eliminar.config(
            command = self.eliminar_venta
        )


    def ventana_registro_cliente(self):
        # Creacion de TopLevel para apertura de ventana
        self.top_level = Toplevel(self.root)
        self.ventana_registro = VentanaMiembros(self.top_level)
        self.top_level.grab_set()

        # Asignacion evento para registrar nuevo miembro
        self.ventana_registro.boton_guardar.config(
            command = self.boton_nuevo_miembro
        )

        # Asignacion de evento para validacion de cliente
        self.ventana_registro.entry_cliente.bind(
            "<KeyRelease>",
            self.validacion_cliente
        )

        # Asignacion de evento para validacion de dni
        self.ventana_registro.entry_documento.bind(
            "<KeyRelease>",
            self.validacion_dni
        )

        # Asignacion de evento para validacion de telefono
        self.ventana_registro.entry_telefono.bind(
            "<KeyRelease>",
            self.validacion_telefono
        )

        # Asignacion de evento para validacion de email
        self.ventana_registro.entry_email.bind(
            "<KeyRelease>",
            self.validacion_email
        )

    
    def validacion_cliente(self, event):
        # Obtencion de cliente
        cliente = self.ventana_registro.entry_cliente.get()

        # Validacion
        cliente_valido = Validaciones.validacion_cliente(cliente)

        if not cliente_valido:
            self.ventana_registro.entry_cliente.config(
                foreground = 'red'
            )

        else:
            self.ventana_registro.entry_cliente.config(
                foreground = 'black'
            )


    def validacion_dni(self, event):
        # Obtencion del dni
        dni = self.ventana_registro.entry_documento.get()

        # Validacion
        dni_validado = Validaciones.validacion_documento(dni)

        if not dni_validado:
            self.ventana_registro.entry_documento.config(
                foreground = 'red'
            )
        else:
            self.ventana_registro.entry_documento.config(
                foreground = 'black'
            )
    

    def validacion_telefono(self, event):
        # Obtencion telefono
        tel = self.ventana_registro.entry_telefono.get()

        # Validacion
        tel_validado = Validaciones.validacion_telefono(tel)

        if not tel_validado:
            self.ventana_registro.entry_telefono.config(
                foreground = 'red'
            )
        else:
            self.ventana_registro.entry_telefono.config(
                foreground = 'black'
            )
    

    def validacion_email(self, event):
        # Obtencion email
        email = self.ventana_registro.entry_email.get()

        # Validacion
        email_validado = Validaciones.validacion_email(email)

        if not email_validado:
            self.ventana_registro.entry_email.config(
                foreground = 'red'
            )
        else:
            self.ventana_registro.entry_email.config(
                foreground = 'black'
            )
    

    def filtrado_consulta_ventas(self):
        # Obtencion de las fechas para filtrado
        fecha_inicio = self.abrir_consulta_ventas.fecha_desde.get()
        fecha_fin = self.abrir_consulta_ventas.fecha_hasta.get()

        # Obtencion de ventas entre fechas elegidas
        ventas_filtro = self.modelo_ventas.consulta_ventas(
            fecha_inicio,
            fecha_fin
        )

        # Verificacion de existencia de resultados
        if not ventas_filtro:
            messagebox.showinfo(
                'Consulta de Ventas',
                'No se encontraron ventas entre las fechas elegidas!'
            )
            self.abrir_consulta_ventas.limpiar_treeview()
            return

        # Limpieza de Treeview
        self.abrir_consulta_ventas.limpiar_treeview()

        # Se agregan ventas filtradas a Treeview
        for venta in ventas_filtro:
            self.abrir_consulta_ventas.treeview_consulta.insert(
                "",
                "end",
                text= venta[0],
                values= (venta[1], venta[2], f'$ {venta[3]}')
            )


    def eliminar_venta(self):
        # Recuperacion de numero de venta segun elemento elegido en Treeview
        self.seleccion = (
            self.abrir_consulta_ventas.treeview_consulta.selection()
        )

        # Comprobacion de seleccion de una venta
        if len(self.seleccion) != 1:
            messagebox.showerror(
                'Consulta de Ventas',
                'Se debe elegir solo una venta para eliminar')
            return
        
        # Obtencion numero de venta
        nro_venta = self.abrir_consulta_ventas.treeview_consulta.item(
            self.seleccion,
            'text'
        )

        # Consulta eliminacion de venta
        consulta = messagebox.askyesno(
            'Eliminar Ventas',
            f'Desea eliminar la venta #{nro_venta}?'
        )

        if consulta:
            # Consulta devolucion de productos a stock
            devolucion = messagebox.askyesno(
                'Eliminar Ventas',
                f'¿Devolver a stock los productos de la venta #{nro_venta}'
            )

            if devolucion:
                productos_vendidos = (
                    self.modelo_ventas.obtener_detalle_ventas(
                        nro_venta
                    )
                )
                # Devolucion de productos a stock
                for producto in productos_vendidos:
                    ModeloInventario.devolver_productos(
                        producto[0], # Codigo
                        producto[1]  # Cantidad vendida  
                    )

            # Eliminacion de venta
            self.modelo_ventas.eliminar_detalle_ventas(nro_venta)
            self.modelo_ventas.eliminar_venta(nro_venta)

            # Mensaje de confirmacion
            messagebox.showinfo(
                'Eliminar Ventas',
                f'Venta #{nro_venta} eliminada correctamente!'
            )

            # Actualizacion de treeview
            self.abrir_consulta_ventas.limpiar_treeview()
            self.filtrado_consulta_ventas()


    def completar_detalle_producto(self, event):
        '''
        Esta funcion esta vinculada a un evento del tipo <KeyRelease> en el
        entry del codigo de la ventana principal de ventas. Se busca la 
        informacion del producto en ModeloInventario y luego se modifica el
        valor text de label_descripcion y label_enstock para mostrar el
        producto y su stock 
        '''
        # Obtencion del codigo ingresado
        codigo = self.vista_ventas.entry_codigo.get()

        # Busqueda de informacion de producto con codigo
        info = ModeloInventario.info_producto(codigo)
        if info:
            # Seteo de labels
            self.vista_ventas.label_descripcion.config(
                text = f'Descripcion: {info[0][0]}'
            )
            self.vista_ventas.label_enstock.config(
                text = f'En Stock: {info[0][2]}'
            )
        else:
            self.vista_ventas.label_descripcion.config(
                text = 'Descripcion: Producto no encontrado'
            )
            self.vista_ventas.label_enstock.config(
                text = 'En Stock: -'
            )


    def boton_agregar_carrito(self):
        try:
            # Obtencion de valores de entry
            codigo = int(self.vista_ventas.entry_codigo.get())
            cantidad = int(self.vista_ventas.entry_cantidad.get())

            # Verificacion de existencia de producto
            producto = ModeloInventario.info_producto(codigo)
            if not producto:
                messagebox.showwarning(
                    'Producto Inexistente',
                    'El producto introducido no existe'
                )
                return
            
            # Propiedades del producto
            descripcion = producto[0][0]
            precio = producto[0][1]
            stock = producto[0][2]

            # Si cantidad > stock, se da mensaje de error
            if cantidad > stock:
                messagebox.showwarning(
                    'Stock Insuficiente',
                    'No se dispone de esa cantidad en stock'
                )
                return

            # Se obtiene subtotal (precio * cantidad)
            subtotal = precio * cantidad

            # Se introduce producto a treeview
            self.vista_ventas.treeview_carrito.insert(
                "",
                "end",
                text = codigo,
                values = (descripcion, f'$ {precio}', cantidad, f' $ {subtotal}')
            )

            # Limpieza de cajas y foco en entry_codigo
            self.vista_ventas.limpiar_cajas()
            self.vista_ventas.entry_codigo.focus()

            # Actualizacion totales de venta
            self.total_venta += subtotal
            self.vista_ventas.label_total_venta.config(
                text = f'Total de venta: $ {self.total_venta}'
            )

            self.total_pagar = self.total_venta
            self.vista_ventas.label_total_a_pagar.config(
                text = f'Total a pagar: $ {self.total_pagar}'
            )

        except ValueError:
            messagebox.showerror('Error','Error en ingreso de datos')
        except Exception as e:
            messagebox.showerror('Error',f'Error inesperado - {e}')


    def boton_eliminar_carrito(self):
        # Obtencion del elemento a eliminar
        seleccion = self.vista_ventas.treeview_carrito.selection()

        # Verificacion de seleccion
        if not seleccion:
            messagebox.showwarning(
                'Eliminar del Carrito',
                'No se ha elegido ningun producto'
            )
            return
        
        # Eliminacion
        for item in seleccion:
            # Obtencion del monto a descontar del monto de venta
            info = self.vista_ventas.treeview_carrito.item((item,), 'values')
            monto_descontar = float(info[3])
            
            # Eliminacion del producto
            self.vista_ventas.treeview_carrito.delete(item)

            # Actualizacion monto de venta
            self.total_pagar -= monto_descontar
            self.total_venta -= monto_descontar

            self.vista_ventas.label_total_a_pagar.config(
                text = f'Total a pagar: ${self.total_pagar}'
            )

            self.vista_ventas.label_total_venta.config(
                text = f'Total de venta: ${self.total_venta}'
            )


    def boton_finalizar_venta(self):

        # Obtencion de fecha venta
        fecha_venta = self.vista_ventas.entry_fecha.get()
        
        # Obtencion de los productos del carrito en una lista
        lista_productos = []
        items = self.vista_ventas.treeview_carrito.get_children()

        # Verificacion si hay productos en carrito
        if not items:
            messagebox.showwarning(
                'Carrito Vacío',
                'El carrito se encuentra vacío, agregar productos!'
            )
            return
        
        consulta_venta = messagebox.askyesno(
            'Finalizacion de venta',
            '¿Desea finalizar la venta?'
        )

        if consulta_venta:

            for item in items:
                codigo = self.vista_ventas.treeview_carrito.item(item, 'text')
                info = self.vista_ventas.treeview_carrito.item(item, 'values')
                cantidad = int(info[2])

                # Se agrega codigo y cantidad a lista_productos
                lista_productos.append((codigo,cantidad))

            # Obtencion del numero de venta
            info_nro_venta = self.modelo_ventas.obtener_nro_venta()
            if info_nro_venta[0][0] is None:
                nro_venta = 1
            else:
                nro_venta = info_nro_venta[0][0] + 1

            # Carga de venta en tabla Ventas
            self.modelo_ventas.nueva_venta(
                nro_venta,
                fecha_venta,
                self.cliente,
                self.total_pagar,
                self.descuento_aplicado
            )

            # Carga productos en Detalle Ventas
            for producto in lista_productos:
                self.modelo_ventas.agregar_detalle_ventas(
                    nro_venta,
                    producto[0],
                    producto[1]
                )

                # Se descuentan productos vendidos de Inventario
                ModeloInventario.descontar_producto(
                    producto[0],
                    producto[1]
                )
            
            # Mensaje de confirmacion
            messagebox.showinfo(
                'Ventas',
                f'Venta #{nro_venta} generada correctamente!'
            )

            # Consulta de registro de cliente como miembro del negocio
            if self.cliente == 0:
                consulta_miembro = messagebox.askyesno(
                    'Miembros',
                    '¿Desea registrar cliente como miembro del supermercado?'
                )
                if consulta_miembro:
                    self.ventana_registro_cliente()

            # Limpieza de campos y seteo de valores
            self.vista_ventas.label_descripcion.config(
                text= "Descripcion:"
            )
            
            self.vista_ventas.label_enstock.config(
                text= "En Stock:"
            )

            self.vista_ventas.label_total_a_pagar.config(
                text= "Total a pagar: $"
            )

            self.vista_ventas.label_total_venta.config(
                text= "Total de venta: $"
            )

            self.vista_ventas.label_descuentos.config(
                text= "Descuentos: $"
            )

            self.vista_ventas.limpiar_treeview()

            self.vista_ventas.limpiar_cliente()

            self.vista_ventas.label_cliente_encontrado.config(
                text= "Cliente: "
            )

            self.total_venta = 0
            self.total_pagar = 0
            self.cliente = 0
            self.descuento_aplicado = 0


    def boton_verificar_cliente(self):
        # Verificacion de que primero haya productos en carrito
        productos_carrito = self.vista_ventas.treeview_carrito.get_children()
        if not productos_carrito:
            messagebox.showwarning(
                'Carrito vacio',
                'Antes de validar cliente, se debe cargar un producto'
            )
            return

        # Obtencion dni de cliente
        cliente = self.vista_ventas.entry_cliente.get()

        # Verificacion que existe en base de clientes
        validacion = self.modelo_ventas.obtener_nombre_cliente(cliente)
        if not validacion:
            self.vista_ventas.label_cliente_encontrado.config(
                text = 'Cliente: No registrado')
            
            self.total_pagar = self.total_venta
            self.vista_ventas.label_descuentos.config(
                text = 'Descuentos: $ 0'
            )

            # El monto a pagar es igual al monto de venta
            self.vista_ventas.label_total_a_pagar.config(
                text = f'Total a pagar: $ {self.total_pagar}'
            )
            
            # Se guarda al cliente inexistente con id = 0
            self.cliente = 0
        
        # Si cliente es miembro, se aplica descuento
        else:   
                # Obtencion nombre de cliente
                nombre_cliente = validacion[0][0]

                # Se verifica que no se aplique descuento mas veces
                if self.cliente != cliente:
                    
                    # Se comienza con monto a pagar = monto venta
                    self.total_pagar = self.total_venta

                    # Se setea nombre de cliente en label
                    self.cliente = cliente
                    self.vista_ventas.label_cliente_encontrado.config(
                        text = f'Cliente: {nombre_cliente}'
                    )
                    
                    # Se calcula descuento y se aplica
                    descuento = ModeloVentas().descuento()[0][0]
                    
                    # Se aplica si supera el monto minimo
                    monto_minimo = ModeloVentas().monto_minimo()[0][0]
                    
                    if self.total_pagar > monto_minimo:
                        self.descuento_aplicado = descuento * self.total_venta
                    else:
                        self.descuento_aplicado = 0
                    
                    self.vista_ventas.label_descuentos.config(
                        text = f'Descuentos: $ {self.descuento_aplicado}'
                    )
                    
                    self.total_pagar -= self.descuento_aplicado
                    self.vista_ventas.label_total_a_pagar.config(
                        text = f'Total a pagar: $ {self.total_pagar}'
                    )
                
                # Si ya se verifico el cliente, se muestra mensaje
                else:
                    messagebox.showwarning(
                        'Cliente Validado',
                        'Ya se ha validado al cliente'
                    )


    def boton_nuevo_miembro(self):
        # Se recuperan entradas de usuario
        cliente = self.ventana_registro.entry_cliente.get()
        dni = self.ventana_registro.entry_documento.get()
        tel = self.ventana_registro.entry_telefono.get()
        email = self.ventana_registro.entry_email.get()

        # Validaciones
        val_cliente = Validaciones.validacion_cliente(cliente)
        val_dni = Validaciones.validacion_documento(dni)
        val_tel = Validaciones.validacion_telefono(tel)
        val_email = Validaciones.validacion_email(email)

        # Verificacion
        if not(val_cliente and val_dni and val_tel and val_email):
            messagebox.showerror(
                'Validacion de nuevo miembro',
                'Verificar campos, no debe haber campos en rojo o vacios!'
            )
            return

        # Carga de cliente
        self.modelo_ventas.registrar_cliente(
            cliente,
            dni,
            tel,
            email
        )

        # Mensaje de confirmacion
        messagebox.showinfo(
            'Nuevo Miembro',
            f'Se ha agregado a {cliente} como miembro del supermercado!'
        )

        # Se cierra ventana de nuevo miembro
        self.top_level.destroy()
    

    def actualizar_descuento_monto(self):
        try:
            # Recuperacion valores de entry
            descuento = float(self.abrir_configuracion.entry_descuento.get())
            monto = int(self.abrir_configuracion.entry_monto.get())

            if descuento >= 1 or descuento < 0:
                messagebox.showerror(
                    'Error',
                    'El descuento debe ser un numero entre 0 y 1'
                )
                return
            
            # Verificacion llenado de campos
            if descuento == '' or monto == '':
                messagebox.showerror(
                    'Error',
                    'Se deben completar los campos'
                )
                return
            
            # Actualizacion de campos
            self.modelo_ventas.nuevo_descuento_monto(descuento, monto)

            # Mensaje de confirmacion y cerrado de ventana
            messagebox.showinfo(
                'Configuracion de descuentos',
                'Informacion de descuentos actualizada'
            )

            self.top_level.destroy()

        except ValueError:
            messagebox.showerror(
                    'Error',
                    'Error en los campos'
                )
            