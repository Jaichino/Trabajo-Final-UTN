import re
from modelo.database import BaseDatos


class ModeloVentas:

    # Atributo de clase para asignar descuento a clientes miembros
    DESCUENTO_MIEMBRO = 0.20

    # Atributo de clase para asignar monto minimo para aplicar descuento
    MONTO_MINIMO = 30000


    @staticmethod
    def nueva_venta(nro_venta,fecha,cliente,monto_total,descuento_miembro):

        query = ''' 
                    INSERT INTO Ventas(nro_venta,fecha,cliente,monto_total,descuento_miembro) VALUES (?,?,?,?,?)

                '''

        BaseDatos.realizar_consulta(query,(nro_venta,fecha,cliente,monto_total,descuento_miembro),None)

    @staticmethod
    def agregar_detalle_ventas(nro_venta,codigo_producto,cantidad):

        query = ''' INSERT INTO DetalleVentas(nro_venta,codigo_producto,cantidad)
                    VALUES (?,?,?)
                '''

        BaseDatos.realizar_consulta(query,
                                    (nro_venta,codigo_producto,cantidad),
                                    None)


    @staticmethod
    def consulta_ventas(fecha_inicio,fecha_final):

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
                                            (fecha_inicio,fecha_final),
                                            "SELECT")

    
    @staticmethod
    def eliminar_venta(nro_venta):
        
        query = ''' DELETE FROM Ventas
                    WHERE nro_venta = ?
                '''

        BaseDatos.realizar_consulta(query, (nro_venta,), None)
        

    @staticmethod
    def eliminar_detalle_ventas(nro_venta):
        
        query = ''' DELETE FROM DetalleVentas
                    WHERE nro_venta = ?
                '''

        BaseDatos.realizar_consulta(query, (nro_venta,), None)


    @staticmethod
    def registrar_cliente(nombre,dni,tel,email):
        
        query = ''' INSERT INTO Clientes(documento,nombre,telefono,email)
                    VALUES(?, ?, ?, ?)
                '''
        
        BaseDatos.realizar_consulta(query, (dni,nombre,tel,email), None)


    @staticmethod
    def obtener_nombre_cliente(dni):
        
        query = ''' SELECT nombre FROM Clientes
                    WHERE documento = ?
                '''
        
        return BaseDatos.realizar_consulta(query,(dni,),'SELECT')
    
    @staticmethod
    def obtener_nro_venta():
        
        query = ''' SELECT MAX(nro_venta)
                    FROM Ventas
                '''
        
        return BaseDatos.realizar_consulta(query,None,'SELECT')
    

    @staticmethod
    def obtener_detalle_ventas(nro_venta):

        query = ''' SELECT
                        codigo_producto,
                        cantidad
                    FROM DetalleVentas
                    WHERE nro_venta = ?
                '''

        return BaseDatos.realizar_consulta(query, (nro_venta,), 'SELECT')











    @staticmethod
    def validacion_cliente(cliente):
        patron = r"^[a-zA-Z\s]+$"
        coincidencia = re.match(patron,cliente)
        return coincidencia
    

    @staticmethod
    def validacion_telefono(telefono):
        patron = r"^\d{2,4}\-\d{7}$"
        coincidencia = re.match(patron,telefono)
        return coincidencia
    

    @staticmethod
    def validacion_email(email):
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        coincidencia = re.match(patron,email)
        return coincidencia
    
    
    @staticmethod
    def validacion_documento(documento):
        patron = r"^\d{8}$"
        coincidencia = re.match(patron,documento)
        return coincidencia
