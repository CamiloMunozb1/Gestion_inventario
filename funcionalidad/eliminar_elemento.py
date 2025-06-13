import sqlite3

class IngresoDB:
    def __init__(self,ruta_db):
        try:
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}.")
    
    def cierre_db(self):
        self.conn.close()

class EliminarElementos:
    def __init__(self,conexion):
        self.conexion = conexion

    def inventario_eliminar(self):
        try:
            nombre_producto = str(input("Ingresa el nombre del producto a eliminar: ")).strip()
            if not nombre_producto:
                print("El campo debe estar completo.")
                return
            self.conexion.cursor.execute("SELECT producto_id FROM productos WHERE nombre_producto = ?",(nombre_producto,))
            producto =  self.conexion.cursor.fetchone()
            if producto:
                producto_id = producto[0]
                self.conexion.cursor.execute("DELETE FROM productos WHERE producto_id = ?",(producto_id,))
                self.conexion.conn.commit()
                print("Producto eliminado con exito.")
            else:
                print("Producto no encontrado, vuelve ingresar uno valido.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            print(f"Error en el programa: {error}.")
