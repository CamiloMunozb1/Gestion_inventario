import sqlite3
import pandas as pd

class IngresoDB:
    def __init__(self,ruta_db):
        try:
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}.")
    
    def cierre_db(self):
        self.conn.close()

class MostrarInventario:
    def __init__(self,conexion):
        self.conexion = conexion

    def motrar_inventario(self):
        try:
            query ="""
                SELECT 
                    nombre_producto,
                    cantidad_producto,
                    nombre_proovedor,
                    precio_compra,
                    fecha_ingreso
                FROM productos
                """
            resultado_df = pd.read_sql_query(query, self.conexion.conn)
            if not resultado_df.empty:
                print(resultado_df)
            else:
                print("No se encontraron registros.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}")
        except Exception as error:
            print(f"Error en el programa : {error}")