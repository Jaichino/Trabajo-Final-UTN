from modelo.database import BaseDatos

class ModeloInventario:

    @staticmethod
    def mostrar_productos():
        query = 'SELECT * FROM Productos WHERE estado = ?'
        return BaseDatos.realizar_consulta(query, ('True',), 'SELECT')


    @staticmethod
    def nuevo_producto(descripcion, precio_unitario, stock):
        query = ''' INSERT INTO Productos (descripcion,precio_unitario,stock)
                    VALUES (?,?,?)
                '''

        BaseDatos.realizar_consulta(query,
                                    (descripcion,precio_unitario,stock),
                                    None)

    
    @staticmethod
    def modificar_producto(descripcion, precio_unitario, stock, codigo_producto):

        query = ''' UPDATE Productos SET descripcion = ?, 
                    precio_unitario = ?, 
                    stock = ?
                    WHERE codigo_producto = ?
                '''
        
        BaseDatos.realizar_consulta(query,
                                    (descripcion,precio_unitario,stock,codigo_producto),
                                    None)

    
    @staticmethod
    def eliminar_producto(codigo_producto):
        query = ''' UPDATE Productos SET estado = 'False'
                    WHERE codigo_producto = ?
                '''

        BaseDatos.realizar_consulta(query, (codigo_producto,), None)
    

    @staticmethod
    def filtrar_productos(codigo=None, descripcion=None):
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
        query = ''' SELECT * FROM Productos 
                    WHERE stock = ? AND estado = ?'''

        return BaseDatos.realizar_consulta(query, (0,'True'), 'SELECT')
    
    
    @staticmethod
    def info_producto(codigo, estado='True'):

        query = ''' SELECT descripcion, precio_unitario, stock
                    FROM Productos WHERE estado = ? AND
                    codigo_producto = ?
                '''
        
        return BaseDatos.realizar_consulta(query, (estado,codigo), 'SELECT')

    @staticmethod
    def descontar_producto(codigo, cantidad):

        query = ''' UPDATE Productos SET stock = stock - cantidad
                    WHERE codigo_producto = ?
                '''
        
        BaseDatos.realizar_consulta(query, (cantidad, codigo), None)