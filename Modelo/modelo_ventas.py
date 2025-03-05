##############################################################################
# Importaciones
##############################################################################

from modelo.database import BaseDatos

##############################################################################
# Clase modelo de ventas
##############################################################################

class ModeloVentas:

    ''' La clase modelo de ventas contiene los metodos necesarios para
        interactuar con la base de datos en lo que respecta al modulo de 
        Ventas de la aplicacion.
    '''

    ##########################################################################
    # Metodos
    ##########################################################################

    @staticmethod
    def nueva_venta(
        nro_venta, 
        fecha, 
        cliente, 
        monto_total, 
        descuento_miembro
    ):
        ''' Metodo que se encarga de insertar un nuevo registro de venta en la
            tabla 'Ventas'.

            :param int nro_venta: Numero de venta realizada.
            :param date fecha: Fecha en la que se lleva a cabo la venta.
            :param int cliente: Numero de documento de cliente. 0 si no esta
                registrado
            :param float monto_total: Monto total de la venta
            :param float descuento_miembro: Descuento aplicado a venta si
                corresponde
        '''

        query = ''' 
                    INSERT INTO Ventas
                    (nro_venta,fecha,cliente,monto_total,descuento_miembro) 
                    VALUES (?,?,?,?,?)
                '''

        BaseDatos.realizar_consulta(query,
                                    (nro_venta,
                                    fecha,
                                    cliente,
                                    monto_total,
                                    descuento_miembro),
                                    None)


    @staticmethod
    def agregar_detalle_ventas(nro_venta, codigo_producto, cantidad):

        ''' Metodo para insertar detalle de una determinada venta en la tabla
            DetalleVentas. Se insertan tantos registros como tipos de producto
            se hayan vendido.

            :param int nro_venta: Referencia al numero de venta
            :param int codigo_producto: Numero de producto vendido.
            :param int cantidad: Cantidad de cada tipo de producto vendido.
        '''

        query = ''' INSERT INTO DetalleVentas
                    (nro_venta,codigo_producto,cantidad)
                    VALUES (?,?,?)
                '''

        BaseDatos.realizar_consulta(query,
                                    (nro_venta, codigo_producto, cantidad),
                                    None)


    @staticmethod
    def consulta_ventas(fecha_inicio, fecha_final):

        ''' Metodo que recopila la informacion de ventas entre dos fechas
            especificadas 'fecha_inicio' y 'fecha_final'.

            :param date fecha_inicio: Fecha inicial de filtrado.
            :param date fecha_final: Fecha final de filtrado.
            :return: Lista con ventas entre dos fechas determinadas.
            :rtype: list

        '''
        query = ''' SELECT 
                        v.nro_venta,
                        v.fecha,
                        c.nombre,
                        v.monto_total
                    FROM Ventas v
                    INNER JOIN Clientes c
                    ON v.cliente = c.documento
                    WHERE v.fecha BETWEEN ? AND ?
                    ORDER BY v.nro_venta
                '''

        return BaseDatos.realizar_consulta(query,
                                            (fecha_inicio, fecha_final),
                                            "SELECT")


    @staticmethod
    def eliminar_venta(nro_venta):
        
        ''' Metodo que elimina una venta determinada de la base de datos,
            tomando como parametro 'nro_venta'.

            :param int nro_venta: Numero de venta a eliminar.
        '''

        query = ''' DELETE FROM Ventas
                    WHERE nro_venta = ?
                '''

        BaseDatos.realizar_consulta(query, (nro_venta,), None)
        

    @staticmethod
    def eliminar_detalle_ventas(nro_venta):

        ''' Metodo para eliminar los detalles de venta correspondientes a un
            determinado 'nro_venta'.

            :param int nro_venta: Numero de venta a eliminar en DetalleVentas.
        '''
        
        query = ''' DELETE FROM DetalleVentas
                    WHERE nro_venta = ?
                '''

        BaseDatos.realizar_consulta(query, (nro_venta,), None)


    @staticmethod
    def registrar_cliente(nombre,dni,tel,email):
        
        ''' Metodo utilizado para registrar nuevos clientes en la base de
            datos.

            :param str nombre: Nombre del nuevo miembro.
            :param int dni: Numero de documento del miembro.
            :param str tel: Numero de telefono del miembro (eg: 351-4567545)
            :param str email: Correo electronico del miembro.
        '''

        query = ''' INSERT INTO Clientes(documento,nombre,telefono,email)
                    VALUES(?, ?, ?, ?)
                '''
        
        BaseDatos.realizar_consulta(query, (dni,nombre,tel,email), None)


    @staticmethod
    def obtener_nombre_cliente(dni):
        
        ''' Metodo utilizado para obtener el nombre de un cliente utilizando
            su numero de documento 'dni'.

            :param int dni: Numero de documento del cliente.
            :return: Lista que contiene el nombre del cliente.
            :rtype: list
        '''

        query = ''' SELECT nombre FROM Clientes
                    WHERE documento = ?
                '''
        
        return BaseDatos.realizar_consulta(query,(dni,),'SELECT')


    @staticmethod
    def obtener_nro_venta():
        
        ''' Metodo utilizado para obtener el ultimo numero de venta de la
            tabla Ventas. Utilizado para tener de referencia para la creacion
            de una nueva venta.

            :return: Lista con ultimo numero de venta de la tabla Ventas.
            :rtype: list
        '''

        query = ''' SELECT MAX(nro_venta)
                    FROM Ventas
                '''
        
        return BaseDatos.realizar_consulta(query,None,'SELECT')


    @staticmethod
    def obtener_detalle_ventas(nro_venta):

        ''' Metodo utilizado para obtener el detalle de productos y cantidad
            vendida en una determinada venta 'nro_venta'.

            :param int nro_venta: Numero de venta a consultar.
            :return: Lista de tuplas que contienen numero de producto
                y cantidades
            :rtype: list
        '''

        query = ''' SELECT
                        codigo_producto,
                        cantidad
                    FROM DetalleVentas
                    WHERE nro_venta = ?
                '''

        return BaseDatos.realizar_consulta(query, (nro_venta,), 'SELECT')
    

    @staticmethod
    def descuento():

        ''' Metodo utilizado para obtener el ultimo descuento agregado,
            siempre que se modifique el valor de descuento aplicado se
            creara un nuevo registro. Este metodo obtiene ese ultimo
            valor.

            :return: Lista que contiene el ultimo descuento aplicado.
            :rtype: list
        '''

        query = ''' SELECT 
                        descuento
                    FROM HistorialDescuentos
                    ORDER BY id DESC
                    LIMIT 1
                '''

        return BaseDatos.realizar_consulta(query, None, 'SELECT')


    @staticmethod
    def monto_minimo():
        
        ''' Metodo que obtiene el ultimo monto minimo necesario para aplicar
            un descuento.

            :return: Lista que contiene el ultimo monto_minimo guardado.
            :rtype: list
        '''

        query = ''' SELECT
                        monto_minimo
                    FROM HistorialDescuentos
                    ORDER BY id DESC
                    LIMIT 1
                '''

        return BaseDatos.realizar_consulta(query, None, 'SELECT')
    

    @staticmethod
    def nuevo_descuento_monto(descuento, monto):

        ''' Metodo que introduce un nuevo registro en la tabla de
            HistorialDescuentos.

            :param float descuento: Descuento a aplicar a ventas de miembros.
            :param int monto: Monto minimo a partir del cual se aplica 
                descuento
        '''
        query = ''' INSERT INTO HistorialDescuentos
                    (descuento, monto_minimo)
                    VALUES (?,?)
                '''
        
        BaseDatos.realizar_consulta(query, (descuento, monto), None)