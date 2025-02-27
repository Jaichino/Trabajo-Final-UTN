##############################################################################
# Importaciones
##############################################################################

import sqlite3

##############################################################################
# Clase conexion con base de datos
##############################################################################

class BaseDatos:

    ##########################################################################
    # Metodos
    ##########################################################################
    
    @staticmethod
    def conexion():
        try:
            conn = sqlite3.connect('Market.db')
            return conn
        except Exception as e:
            print(f'Error al conectarse con la base de datos - {e}')
    

    @staticmethod
    def cerrar_conexion(conn):
        if conn:
            conn.close()
    

    @staticmethod
    def realizar_consulta(sql, valores=None, tipo=None):
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
