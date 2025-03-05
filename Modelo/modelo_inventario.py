##############################################################################
# Importaciones
##############################################################################

from modelo.database import BaseDatos

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
    def mostrar_productos():
        
        ''' Metodo para obtener toda la informacion de productos de la tabla
            'Productos', donde su 'estado' sea igual a 'True' (productos
            activos).

            :return: Lista de productos disponibles.
            :rtype: list
        '''
        query = 'SELECT * FROM Productos WHERE estado = ?'
        return BaseDatos.realizar_consulta(query, ('True',), 'SELECT')


    @staticmethod
    def nuevo_producto(descripcion, precio_unitario, stock):

        ''' Metodo para la creacion de nuevos productos en la base de datos.
            Se toma como parametros 'descripcion', 'precio_unitario' y 'stock'
            
            :param str descripcion: Descripcion del producto.
            :param float precio_unitario: Precio unitario del producto.
            :param int stock: Stock disponible del producto.
        '''

        query = ''' INSERT INTO Productos (descripcion,precio_unitario,stock)
                    VALUES (?,?,?)
                '''

        BaseDatos.realizar_consulta(query,
                                    (descripcion,precio_unitario,stock),
                                    None)

    
    @staticmethod
    def modificar_producto(
        descripcion, 
        precio_unitario, 
        stock, 
        codigo_producto
    ):
        
        ''' Metodo para realizar la modificacion de un producto existente en
            la base de datos.

            :param str descripcion: Descripcion del producto.
            :param float precio_unitario: Precio unitario del producto.
            :param int stock: Stock del producto.
            :param int codigo_producto: Codigo del producto a modificar.
        '''

        query = ''' UPDATE Productos SET descripcion = ?, 
                    precio_unitario = ?, 
                    stock = ?
                    WHERE codigo_producto = ?
                '''
        
        BaseDatos.realizar_consulta(query,
                                    (descripcion,
                                    precio_unitario,
                                    stock,
                                    codigo_producto),
                                    None)


    @staticmethod
    def eliminar_producto(codigo_producto):

        ''' Metodo para eliminar un producto de la base de datos. Toma como
            parametro el 'codigo_producto'

            :param int codigo_producto: Codigo del producto a eliminar.
        '''

        query = ''' UPDATE Productos SET estado = 'False'
                    WHERE codigo_producto = ?
                '''

        BaseDatos.realizar_consulta(query, (codigo_producto,), None)


    @staticmethod
    def filtrar_productos(codigo=None, descripcion=None):

        ''' Metodo para filtrar productos segun su 'codigo' o segun una
            coincidencia en su 'descripcion'. Por defecto, ambos parametros
            son None. Si ambos se dejan como None, el metodo dara como
            resultado todos los productos.

            :param int codigo: Codigo del producto
            :param str desripcion: Descripcion del producto
            :return: Lista de productos filtrados.
            :rtype: list
        '''

        params = ['True']
        query = 'SELECT * FROM Productos WHERE estado = ?'
        
        if codigo is not None:
            query += ' AND codigo_producto = ?'
            params.append(codigo)
        
        if descripcion is not None:
            query += ' AND descripcion LIKE ? COLLATE NOCASE'
            params.append(f'%{descripcion}%')
        
        query += ' ORDER BY descripcion'

        return BaseDatos.realizar_consulta(query, params, 'SELECT')


    @staticmethod
    def productos_sin_stock():

        ''' Metodo para obtener todos aquellos productos cuyo stock es igual
            a cero.

            :return: Lista de productos con stock igual a cero.
            :rtype: list
        '''

        query = ''' SELECT * FROM Productos 
                    WHERE stock = ? AND estado = ?'''

        return BaseDatos.realizar_consulta(query, (0,'True'), 'SELECT')


    @staticmethod
    def info_producto(codigo, estado='True'):

        ''' Metodo para obtener la informacion de un producto determinado
            mediante su 'codigo' y cuando su 'estado' sea igual a True.

            :param int codigo: Codigo del producto.
            :param bool estado: Estado del producto
            :return: Lista informacion de producto determinado.
            :rtype: list
        '''

        query = ''' SELECT descripcion, precio_unitario, stock
                    FROM Productos WHERE estado = ? AND
                    codigo_producto = ?
                '''
        
        return BaseDatos.realizar_consulta(query, (estado,codigo), 'SELECT')


    @staticmethod
    def descontar_producto(codigo, cantidad):

        ''' Metodo para restar los productos que fueron vendidos en una venta
            determinada.

            :param int codigo: Codigo de producto vendido
            :param int cantidad: Cantidad vendida del producto.
        '''

        query = ''' UPDATE Productos SET stock = stock - ?
                    WHERE codigo_producto = ?
                '''
        
        BaseDatos.realizar_consulta(query, (cantidad, codigo), None)


    @staticmethod
    def devolver_productos(codigo, cantidad):

        ''' Metodo para devolver a stock los productos en caso de que una
            venta sea eliminada.

            :param int codigo: Codigo de producto a devolver.
            :param int cantidad: Cantidad a devolver del producto.
        '''

        query = ''' UPDATE Productos SET stock = stock + ?
                    WHERE codigo_producto = ?
                '''
        
        BaseDatos.realizar_consulta(query, (cantidad, codigo), None)
