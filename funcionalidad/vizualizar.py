import sqlite3 # Importacion de SQLite3 para manejar la base de datos.
import pandas as pd # Importacion de pandas para visualizar los datos.

class IngresoDB:
    def __init__(self,ruta_db):
        try:
            # Conexion con la base de datos.
            self.conn = sqlite3.connect(ruta_db)
            # Se crea un cursor para manejar la base de datos.
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}.")
    
    def cierre_db(self):
        # Cierre de la base de datos.
        self.conn.close()

class MostrarInventario:
    def __init__(self,conexion):
        # Se le pasa la conexion con la base de datos.
        self.conexion = conexion

    def motrar_inventario(self):
        try:
            # Query o consulta para seleccionar los campos de la base de datos.
            query ="""
                SELECT 
                    nombre_producto,
                    cantidad_producto,
                    nombre_proovedor,
                    precio_compra,
                    fecha_ingreso
                FROM productos;
                """
            # Se lee la query con pandas y el cursor para acceder a la informacion.
            resultado_df = pd.read_sql_query(query, self.conexion.conn)
            # Si la peticion no esta vacia muestra los resultados.
            if not resultado_df.empty:
                print(resultado_df)
            else:
                print("No se encontraron registros.")
        # Manejo de errores.
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}")
        except Exception as error:
            print(f"Error en el programa : {error}")