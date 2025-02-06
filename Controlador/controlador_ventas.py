from tkinter import *
from tkinter import messagebox
from modelo.modelo_ventas import ModeloVentas
from modelo.modelo_inventario import ModeloInventario
from vista.vista_ventas import VentanaVentas, VentanaConsultaVentas, VentanaMiembros

class ControladorVentas:
    
    def __init__(self,root):
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

        # Asignacion de evento a entry_codigo
        self.vista_ventas.entry_codigo.bind(
            "<KeyRelease>", 
            self.completar_detalle_producto
            )
        
        # Asignacion de funcion agregar a carrito
        self.vista_ventas.boton_agregar_carrito.config(
            command = self.boton_agregar_carrito
        )

        # Asignacion de funcion a boton validar cliente
        self.vista_ventas.boton_validar_cliente.config(
            command = self.boton_validar_cliente
        )

    
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
                values = (descripcion, precio, cantidad, subtotal)
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


    def boton_validar_cliente(self):

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
            
            # Se setea descuento en $0
            descuento = 0
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
                    descuento = ModeloVentas().DESCUENTO_MIEMBRO
                    
                    # Se aplica si supera el monto minimo
                    monto_minimo = ModeloVentas().MONTO_MINIMO
                    
                    if self.total_venta > monto_minimo:
                        descuento_aplicado = descuento * self.total_venta
                    else:
                        descuento_aplicado = 0
                    
                    self.vista_ventas.label_descuentos.config(
                        text = f'Descuentos: $ {descuento_aplicado}'
                    )
                    
                    self.total_pagar -= descuento_aplicado
                    self.vista_ventas.label_total_a_pagar.config(
                        text = f'Total a pagar: $ {self.total_pagar}'
                    )
                
                # Si ya se verifico el cliente, se muestra mensaje
                else:
                    messagebox.showwarning(
                        'Cliente Validado',
                        'Ya se ha validado al cliente'
                    )
