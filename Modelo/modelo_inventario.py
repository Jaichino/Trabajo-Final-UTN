##############################################################################
# Importaciones
##############################################################################

from sqlmodel import Session, select
from modelo.database import engine, Producto
from modelo.logging_decorador import registro_logging
from modelo.logging_observador import logger

##############################################################################
# Clase modelo de inventario
##############################################################################

class ModeloInventario:

    ''' La clase modelo de inventario contiene los metodos necesarios para
        interactuar con la base de datos en lo que respecta al modulo de 
        Inventario de la aplicacion.
    '''

    ##########################################################################
    # Metodos
    ##########################################################################

    @staticmethod
    def mostrar_productos(estado: int=True):
        
        ''' Metodo para obtener toda la informacion de productos de la tabla
            'Productos', donde su 'estado' sea igual a 'True' (productos
            activos).

            :return: Lista de productos disponibles.
            :rtype: list
        '''
        with Session(engine) as sesion:
            productos = sesion.exec(
                select(Producto).where(Producto.estado == estado)
            ).all()

            return productos


    @staticmethod
    @registro_logging("Producto creado")
    def nuevo_producto(
        descripcion: str, 
        precio_unitario: float, 
        stock: int, 
        estado: bool=True
    ):

        ''' Metodo para la creacion de nuevos productos en la base de datos.
            Se toma como parametros 'descripcion', 'precio_unitario' y 'stock'
            
            :param str descripcion: Descripcion del producto.
            :param float precio_unitario: Precio unitario del producto.
            :param int stock: Stock disponible del producto.
            :param bool estado: Estado de disponibilidad de producto.
        '''

        with Session(engine) as sesion:
            producto = Producto(
                descripcion=descripcion,
                precio_unitario=precio_unitario,
                stock=stock,
                estado=estado
            )
            sesion.add(producto)
            sesion.commit()

            logger.log(
                "Producto creado", args=(descripcion, precio_unitario, stock)
            )


    @staticmethod
    @registro_logging("Producto modificado")
    def modificar_producto(
        descripcion: str, 
        precio_unitario: float, 
        stock: int, 
        id_prod: int
    ):
        
        ''' Metodo para realizar la modificacion de un producto existente en
            la base de datos.

            :param str descripcion: Descripcion del producto.
            :param float precio_unitario: Precio unitario del producto.
            :param int stock: Stock del producto.
            :param int id_prod: Codigo del producto a modificar.
        '''
        with Session(engine) as sesion:

            producto_modificar = sesion.exec(
                select(Producto).where(Producto.codigo_producto == id_prod)
            ).one()

            producto_modificar.descripcion = descripcion
            producto_modificar.precio_unitario = precio_unitario
            producto_modificar.stock = stock

            sesion.add(producto_modificar)
            sesion.commit()

            logger.log(
                "Producto modificado", 
                args= (descripcion, precio_unitario, stock, id_prod)
            )


    @staticmethod
    @registro_logging("Producto eliminado")
    def eliminar_producto(id_prod: int):

        ''' Metodo para eliminar un producto de la base de datos. Toma como
            parametro el 'codigo_producto'

            :param int codigo_producto: Codigo del producto a eliminar.
        '''

        with Session(engine) as sesion:
            producto_eliminar = sesion.exec(
                select(Producto).where(Producto.codigo_producto == id_prod)
            ).one()

            producto_eliminar.estado = False
            sesion.add(producto_eliminar)
            sesion.commit()

            logger.log("Producto eliminado", args=(id_prod))


    @staticmethod
    def filtrar_productos(codigo: int=None, descripcion: str=None):

        ''' Metodo para filtrar productos segun su 'codigo' o segun una
            coincidencia en su 'descripcion'. Por defecto, ambos parametros
            son None. Si ambos se dejan como None, el metodo dara como
            resultado todos los productos.

            :param int codigo: Codigo del producto
            :param str desripcion: Descripcion del producto
            :return: Lista de productos filtrados.
            :rtype: list
        '''

        with Session(engine) as sesion:

            query = select(Producto).where(Producto.estado == True)

            if codigo is not None:
                query = query.where(Producto.codigo_producto == codigo)

            if descripcion is not None:
                query = query.where(
                    Producto.descripcion.like(f"%{descripcion}%")
                    )

            productos = sesion.exec(query).all()
            return productos


    @staticmethod
    def productos_sin_stock(stock: int=0, estado: bool=True):

        ''' Metodo para obtener todos aquellos productos cuyo stock es igual
            a cero.

            :return: Lista de productos con stock igual a cero.
            :rtype: list
        '''
        with Session(engine) as sesion:

            prod_sin_stock = sesion.exec(
                select(Producto)
                .where(Producto.stock == stock)
                .where(Producto.estado == estado)
            ).all()

            return prod_sin_stock


    @staticmethod
    def info_producto(codigo: int, estado=True):

        ''' Metodo para obtener la informacion de un producto determinado
            mediante su 'codigo' y cuando su 'estado' sea igual a True.

            :param int codigo: Codigo del producto.
            :param bool estado: Estado del producto
            :return: Lista informacion de producto determinado.
            :rtype: list
        '''
        with Session(engine) as sesion:
            info = sesion.exec(
                select(Producto)
                .where(Producto.codigo_producto == codigo)
                .where(Producto.estado == estado)
            ).first()

            return info


    @staticmethod
    def descontar_producto(codigo: int, cantidad: int):

        ''' Metodo para restar los productos que fueron vendidos en una venta
            determinada.

            :param int codigo: Codigo de producto vendido
            :param int cantidad: Cantidad vendida del producto.
        '''
        with Session(engine) as sesion:
            producto_vendido = sesion.exec(
                select(Producto).where(Producto.codigo_producto == codigo)
            ).one()

            producto_vendido.stock -= cantidad
            sesion.add(producto_vendido)
            sesion.commit()


    @staticmethod
    def devolver_productos(codigo: int, cantidad: int):

        ''' Metodo para devolver a stock los productos en caso de que una
            venta sea eliminada.

            :param int codigo: Codigo de producto a devolver.
            :param int cantidad: Cantidad a devolver del producto.
        '''
        with Session(engine) as sesion:
            producto_a_devolver = sesion.exec(
                select(Producto).where(Producto.codigo_producto == codigo)
            ).one()

            producto_a_devolver.stock += cantidad
            sesion.add(producto_a_devolver)
            sesion.commit()
