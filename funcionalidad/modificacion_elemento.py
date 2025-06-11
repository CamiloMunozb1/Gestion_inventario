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
            "2" : self.modificar_cantidad,
            "3" : self.modificar_proovedor,
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
    
    def modificar_cantidad(self):
        try:
            cantidad_actual = int(input("Ingresa la cantidad ingresada previamente: "))
            cantidad_producto = int(input("Ingresa la cantidad nueva: "))
            if not cantidad_actual or not cantidad_producto:
                print("Los campos deben estar completos.")
                return
            self.conexion.cursor.execute("SELECT 1 FROM productos WHERE cantidad_producto = ?",(cantidad_producto,))
            if self.conexion.cursor.fetchone():
                print("La cantidad del producto ya existe en el campo seleccionado. Por favor, ingresar uno diferente.")
                return
            self.conexion.cursor.execute("UPDATE productos SET cantidad_producto = ? WHERE cantidad_producto = ?",(cantidad_producto,cantidad_actual))
            if self.conexion.cursor.rowcount == 0:
                print("No se encontro la cantidad del producto actual.")
                return
            else:
                self.conexion.conn.commit()
                print("Cantidad del producto modificada exitosamente.")
        except Exception as error:
            print(f"Error en el programa : {error}.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}.")
    
    def modificar_proovedor(self):
        try:
            proovedor_actual = str(input("Ingresa el nombre del proovedor ingresada preeviamente: ")).strip()
            nombre_proovedor = str(input("Ingresa el nombre del proovedor: ")).strip()
            if not proovedor_actual or not nombre_proovedor:
                print("Los campos deben estar completos.")
                return
            self.conexion.cursor.execute("SELECT 1 FROM productos WHERE nombre_proovedor = ?",(nombre_proovedor,))
            if self.conexion.cursor.fetchone():
                print("El nombre del proovedor ya existe en el campo seleccionado. Por favor, ingresar uno diferente.")
                return
            self.conexion.cursor.execute("UPDATE productos SET nombre_proovedor = ? WHERE nombre_proovedor = ?",(nombre_proovedor,proovedor_actual))
            if self.conexion.cursor.rowcount == 0:
                print("No se encontro el nombre del proovedor.")
                return
            else:
                self.conexion.conn.commit()
                print("Nombre del proovedor del producto modificado exitosamente.")
        except Exception as error:
            print(f"Error en el programa : {error}.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}.")

    
    

