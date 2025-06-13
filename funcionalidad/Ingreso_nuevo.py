import sqlite3
from datetime import datetime



class IngresoDB:
    def __init__(self,ruta_db):
        try:
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error de conexion en la base de datos: {error}.")
    
    def cierre_db(self):
        self.conn.close()



class IngresoProductos:
    def __init__(self,conexion):
        self.conexion = conexion
    
    def ingresos_productos(self):
        try:

            nombre_producto = str(input("Ingresa el nombre del producto: ")).strip()
            cantidad_producto = int(input("Ingresa la cantidad del producto: "))
            nombre_proovedor = str(input("Ingresa el nombre del proovedor: ")).strip()
            precio_compra = float(input("Ingresa el precio del monto de productos: "))
            fecha_ingreso = str(input("Ingresa la fecha de ingreso de los productos en formato (DD/MM/AAAA): ")).strip()

            if not all([nombre_producto,cantidad_producto,nombre_proovedor,precio_compra,fecha_ingreso]):
                print("Todos los campos deben estar ingresados.")
                return
            try:
                datetime.strptime(fecha_ingreso, "%d/%m/%Y")
            except ValueError:
                print("Fecha no valida, por favor ingresar nuevamente.")
                return
            
            self.conexion.cursor.execute("SELECT 1 FROM productos WHERE nombre_producto = ?",(nombre_producto,))
            if self.conexion.cursor.fetchone():
                print("Ya se ingreso el nombre del producto, si es el mismo pero con caracteristicas diferentes especificar en el nombre.")
                return
            self.conexion.cursor.execute("INSERT INTO productos(nombre_producto,cantidad_producto,nombre_proovedor,precio_compra,fecha_ingreso) VALUES (?,?,?,?,?)"
                                        ,(nombre_producto,cantidad_producto,nombre_proovedor,precio_compra,fecha_ingreso))
            self.conexion.conn.commit()
            print("Productos ingresados exitosamente.")

        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            print(f"Error en el programa: {error}.")

