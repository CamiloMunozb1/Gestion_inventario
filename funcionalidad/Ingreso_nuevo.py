import sqlite3  # Importacion de SQLite3 para manejo de la base de datos.
from datetime import datetime # Importacion del modulo Datetime para validar fechas.



class IngresoDB:
    def __init__(self,ruta_db):
        try:
            # Conexion a la base de datos.
            self.conn = sqlite3.connect(ruta_db)
            # Cursor para manejo de la base de datos.
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error de conexion en la base de datos: {error}.")
    
    def cierre_db(self):
        # Cierre de la base de datos.
        self.conn.close()



class IngresoProductos:
    def __init__(self,conexion):
        self.conexion = conexion # Recibe la conexion a la base de datos.
    
    def ingresos_productos(self):
        try:
            # Entradas de usuario.
            nombre_producto = str(input("Ingresa el nombre del producto: ")).strip()
            cantidad_producto = int(input("Ingresa la cantidad del producto: "))
            nombre_proovedor = str(input("Ingresa el nombre del proovedor: ")).strip()
            precio_compra = float(input("Ingresa el precio del monto de productos: "))
            fecha_ingreso = str(input("Ingresa la fecha de ingreso de los productos en formato (DD/MM/AAAA): ")).strip()

            # Se valida de que la cantidad del producto no sea menor o igual a 0.
            if cantidad_producto <= 0:
                print("La cantidad del lote del producto no puede ser igual o menos a 0.")
                return
            # Se valida que el precio del monto no sea menor o igual a 0.
            elif precio_compra <= 0:
                print("El precio del lote del producto no puede ser menor o igual a 0.")
                return
            # Campo de validacion de datos.
            elif not all([nombre_producto,cantidad_producto,nombre_proovedor,precio_compra,fecha_ingreso]):
                print("Todos los campos deben estar completos.")
                return
            try:
                datetime.strptime(fecha_ingreso, "%d/%m/%Y") # Validacion de fecha con el formato requerido.
            except ValueError:
                print("Fecha no valida, por favor ingresar nuevamente.")
                return
            
            # Verificacion de elemento por si se encuentra ya ingresado.
            self.conexion.cursor.execute("SELECT 1 FROM productos WHERE nombre_producto = ?",(nombre_producto,))
            if self.conexion.cursor.fetchone():
                print("Ya se ingreso el nombre del producto, si es el mismo pero con caracteristicas diferentes especificar en el nombre.")
                return
            # Ingreso de los datos ingresados por el usuario a la base de datos.
            self.conexion.cursor.execute("INSERT INTO productos(nombre_producto,cantidad_producto,nombre_proovedor,precio_compra,fecha_ingreso) VALUES (?,?,?,?,?)"
                                        ,(nombre_producto,cantidad_producto,nombre_proovedor,precio_compra,fecha_ingreso))
            self.conexion.conn.commit()
            print("Productos ingresados exitosamente.")

        # Manejo de errores.
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            print(f"Error en el programa: {error}.")

