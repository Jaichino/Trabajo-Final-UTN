##############################################################################
# Importaciones
##############################################################################

import sqlite3

##############################################################################
# Clase conexion con base de datos
##############################################################################

class BaseDatos:

    ''' Clase que contiene los metodos necesarios para establecer la conexion
        con la base de datos y de la interaccion con la misma.
    '''

    ##########################################################################
    # Metodos
    ##########################################################################
    
    @staticmethod
    def conexion():
        
        ''' Metodo para establecer conexion con la base de datos.
            :return: Conexion a base de datos.
        '''
        try:
            conn = sqlite3.connect('Market.db')
            return conn
        except Exception as e:
            print(f'Error al conectarse con la base de datos - {e}')
    

    @staticmethod
    def cerrar_conexion(conn):
        
        ''' Metodo encargado de cerrar la conexion a la base de datos.
        '''
        if conn:
            conn.close()
    

    @staticmethod
    def realizar_consulta(sql, valores=None, tipo=None):
        
        ''' Metodo encargado de realizar consultas SQL a la base de datos.
            Primero se establece la conexion utilizando el metodo 'conexion',
            luego se crea un cursor y se ejecuta la consulta con parametros
            especificados, los cuales pueden ser None. El tercer parametro
            del metodo por defecto es None, en caso de ser 'SELECT' retorna
            un resultado mediante el metodo fetchall.

            :return: Cambios en la base de datos, retorno de resultado para
                consultas del tipo 'SELECT'.
        '''
        conn = BaseDatos.conexion()
        if conn:
            try:
                cursor = conn.cursor()
                if valores:
                    cursor.execute(sql,valores)
                else:
                    cursor.execute(sql)

                conn.commit()

                if tipo == "SELECT":
                    resultado = cursor.fetchall()
                    return resultado
            
            except Exception as e:
                print(f"Error al realizar consulta - {e}")
                conn.rollback()
            
            finally:
                cursor.close()
                BaseDatos.cerrar_conexion(conn)
