import os
import mysql.connector
from mysql.connector import Error
#Realizar La Conexion A la Base de datos
class ConexionDb:
    _Conf = {
        'host': 'localhost',
        'user': 'root',
        'password': os.environ.get('DB_PASSWORD', ''),
        'database': 'dbtienda',        
        'port': 3306                     
    }

    @staticmethod
    def ObteniendoConexion():
        try:
            Conectar = mysql.connector.connect(**ConexionDb._Conf)
            return Conectar
        except Error as err:
            raise Exception (f"Error en la conexion de la Base De Datos: {err}")
    
    @staticmethod
    def ejecutar_sp_resultado(nombre_sp: str, parametros: list = None) -> list[dict]:
        conexion = None
        cursor = None
        resultados = []
        try:
            conexion = ConexionDb.ObteniendoConexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc(nombre_sp, parametros or [])

            for result in cursor.stored_results():
                resultados = result.fetchall()

            conexion.commit()
            return resultados
        except Error as err:
            if conexion and conexion.is_connected():
                conexion.rollback()
            raise Exception(f"Fallo en la ejecución del procedimiento almacenado [{nombre_sp}]: {err}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()
