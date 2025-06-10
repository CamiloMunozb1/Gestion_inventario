import sqlite3
from datetime import datetime

class IngresoDB:
    def __init__(self,ruta_db):
        try:
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la conexion con la base de datos: {error}.")
    
    def cierre_db(self):
        self.conn.close()
        print("cierre de la base de datos exitoso.")

class CambiosElementos:
    def __init__(self,conexion):
        self.conexion = conexion
        self.opciones = {
            "1" : self.modificar_nombre,
            "2" : self.opcion_dos,
            "3" : self.opcion_tres,
            "4" : self.opcion_cuatro,
            "5" : self.opcion_cinco,
            "6" : self.opcion_seis
        }
        self.mostar_opciones()
        self.eleccion_usuario()

    def mostar_opciones(self):
        print("""
            Que elemento desea cambiar:
                1. Nombre del producto.
                2. Cantidad del producto.
                3. nombre del proveedor.
                4. El precio del monto.
                5. La fecha de la compra.
                6. Salir.
            """)
    
    def eleccion_usuario(self):
        try:
            while True:
                usuario = str(input("Ingresa la opcion que desees: ")).strip()
                if not usuario:
                    print("El campo debe estar completo.")
                    continue
                accion = self.opciones.get(usuario)
                if accion:
                    accion()
                    if usuario == "6":
                        break
                else:
                    print("Escoge una opcion entre 1 al 6.")
        except ValueError:
            print("Error de digitacion, volver a intentar.")
    
    def modificar_nombre(self):
        try:
            nombre_usado = str(input("Ingresa el nombre del producto que quieres cambiar: ")).strip()
            nombre_producto = str(input("Ingresa el nuevo nombre del producto: ")).strip()
            if not nombre_usado or not nombre_producto:
                print("El campo debe estar completo.")
                return
            self.conexion.cursor.execute("SELECT 1 FROM productos WHERE nombre_producto = ?",(nombre_producto,))
            if self.conexion.cursor.fetchone():
                print("El nuevo nombre ya existe. Por favor, ingresa uno diferente.")
                return
            self.conexion.cursor.execute("UPDATE productos SET nombre_producto = ? WHERE nombre_producto = ?",(nombre_producto, nombre_usado))
            if self.conexion.cursor.rowcount == 0:
                print("No se encontró un producto con ese nombre actual.")
            else:
                self.conexion.conn.commit()
                print("Nombre del producto modificado correctamente.")
        except Exception as error:
            print(f"Error en el programa : {error}.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}.")
    
    

