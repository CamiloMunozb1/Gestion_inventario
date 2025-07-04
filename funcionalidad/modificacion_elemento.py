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
            print(f"Error en la conexion con la base de datos: {error}.")
    
    def cierre_db(self):
        # Cierre de la base de datos.
        self.conn.close()

class CambiosElementos:
    def __init__(self,conexion):
        self.conexion = conexion # Recibe la conexion a la base de datos.
        # Opciones para el usuario.
        self.opciones = {
            "1" : self.modificar_nombre,
            "2" : self.modificar_cantidad,
            "3" : self.modificar_proovedor,
            "4" : self.modificar_monto,
            "5" : self.modificar_fecha,
            "6" : self.salir_programa
        }
        self.mostar_opciones() # Mostrar las opciones al usuario.
        self.eleccion_usuario() # Registra la eleccion del usuario.

    # Opciones las cuales se le mostraran al usuario.
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
                # Ingreso de opcion al usuario
                usuario = str(input("Ingresa la opcion que desees: ")).strip()
                # Campo de validacion.
                if not usuario:
                    print("El campo debe estar completo.")
                    continue
                # Guarda la accion del usuario en una variable y la abrimos en el diccionario.
                accion = self.opciones.get(usuario)
                # Buscar la accion y ejecutarla
                if accion:
                    accion()
                else:
                    # Se revisa la opcion seleccionada y que corresponda al rango.
                    print("Escoge una opcion entre 1 al 6.")
        # Manejo de errores.
        except ValueError:
            print("Error de digitacion, volver a intentar.")
    
    def modificar_nombre(self):
        try:
            # Entrada de usuario.
            nombre_usado = str(input("Ingresa el nombre del producto que quieres cambiar: ")).strip()
            nombre_producto = str(input("Ingresa el nuevo nombre del producto: ")).strip()

            # Se revisa que el nombre no sea igual al acual.
            if nombre_usado == nombre_producto:
                print("El nombre es igual al actual por favor ingresar uno nuevo.")
                return
            # Campo de validacion de la entrada.
            elif not nombre_usado or not nombre_producto:
                print("El campo debe estar completo.")
                return
            # Verificacion de entrada donde se buscara si el nombre del producto ya se encuentra ingresado.
            self.conexion.cursor.execute("SELECT 1 FROM productos WHERE nombre_producto = ?",(nombre_usado,))
            if not self.conexion.cursor.fetchone():
                print("El nuevo nombre no se encontro. ")
                return
            
            # Se actualiza el nombre del producto seleccionado.
            self.conexion.cursor.execute("UPDATE productos SET nombre_producto = ? WHERE nombre_producto = ?",(nombre_producto, nombre_usado))
            # Si se encuentra el nombre del producto se suben los cambios
            self.conexion.conn.commit()
            print("Nombre del producto modificado correctamente.")
        # Manejo de errores.
        except Exception as error:
            print(f"Error en el programa : {error}.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}.")
    
    def modificar_cantidad(self):
        try:
            # Entrada de usuario.
            nombre_producto = str(input("Ingresa el nombre del producto : ")).strip()
            cantidad_actual = int(input("Ingresa la cantidad ingresada previamente: "))
            cantidad_producto = int(input("Ingresa la cantidad nueva: "))

            # Se revisa que la cantidad no sea igual a la anterior.
            if cantidad_actual == cantidad_producto:
                print("La cantidad del producto es igual a la actual, por favor ingresar una nueva.")
                return
            # Se revisa qye la cantidad del producto no sea menor o igual a 0.
            elif cantidad_producto <= 0:
                print("La cantidad del producto no puede ser 0.")
                return
            # Validacion de campos.
            elif not all([nombre_producto,cantidad_actual,cantidad_producto]):
                print("Los campos deben estar completos.")
                return

            # Verificacion donde se busca tanto el nombre como la cantidad actual.
            self.conexion.cursor.execute("SELECT 1 FROM productos WHERE nombre_producto = ? AND cantidad_producto = ?",(nombre_producto,cantidad_actual))
            if not self.conexion.cursor.fetchone():
                print("No se encontró el producto con ese nombre y cantidad actual.")
                return
            
            # Se actualiza la cantidad del producto.
            self.conexion.cursor.execute("UPDATE productos SET cantidad_producto = ? WHERE nombre_producto = ? AND cantidad_producto = ?",(cantidad_producto,nombre_producto,cantidad_actual))
            # Se suben los cambios a la base de datos.
            self.conexion.conn.commit()
            print("Cantidad del producto modificada exitosamente.")

        # Manejo de erroes.
        except Exception as error:
            print(f"Error en el programa : {error}.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}.")
    
    def modificar_proovedor(self):
        try:
            # Entradas de usuario.
            nombre_producto = str(input("Ingresa el nombre del producto : ")).strip()
            proovedor_actual = str(input("Ingresa el nombre del proveedor ingresada preeviamente: ")).strip()
            nombre_proovedor = str(input("Ingresa el nombre del proveedor: ")).strip()


            # Se revisa que el proveedor no sea igual al anterior.
            if proovedor_actual == nombre_proovedor:
                print("El nombre del proveedor es igual al acutal, por favor ingresa uno diferente.")
                return
            
            # Campos de Validacion de usuario.
            elif not all([nombre_producto,proovedor_actual,nombre_proovedor]):
                print("Los campos deben estar completos.")
                return
            
            # Se verifica que el nombre del producto y el nombre del proveedor exita.
            self.conexion.cursor.execute("SELECT 1 FROM productos WHERE nombre_producto = ? AND nombre_proovedor = ?",(nombre_producto,proovedor_actual))
            if not self.conexion.cursor.fetchone():
                print("No se encontró el producto con ese nombre y el proovedor actual.")
                return
            
            # Se actualiza el nombre del proveedor
            self.conexion.cursor.execute("UPDATE productos SET nombre_proovedor = ? WHERE nombre_producto = ? AND nombre_proovedor = ?",(nombre_proovedor,nombre_producto,proovedor_actual))
            # Se suben las cambios a la base de datos.
            self.conexion.conn.commit()
            print("Nombre del proovedor del producto modificado exitosamente.")

        # Manejo de errores.
        except Exception as error:
            print(f"Error en el programa : {error}.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}.")
    
    def modificar_monto(self):
        try:
            # Entrada de usuario.
            nombre_producto = str(input("Ingresa el nombre del producto : ")).strip()
            monto_actual = float(input("Ingresa el monto actual de los productos: "))
            precio_compra = float(input("Ingresa el precido del monto de los productos: "))

            # Se verifica que el valor de la compra no sea igual al anterior.
            if monto_actual == precio_compra:
                print("El monto del precio es igual al actual, por favor ingresa uno diferente.")
                return
            # Se verifica que el monto no sea menor o igual a 0.
            elif precio_compra <= 0:
                print("El valor del monto no puede ser igual o menos a 0.")
                return
            # Validacion de campos.
            elif not all([nombre_producto,monto_actual,precio_compra]):
                print("Los campos deben estar completos.")
                return
            
            # Se busca que el nombre del producto como el monto del producto exista.
            self.conexion.cursor.execute("SELECT 1 FROM productos WHERE nombre_producto = ? AND precio_compra = ?",(nombre_producto,monto_actual))
            if not self.conexion.cursor.fetchone():
                print("No se encontró el producto con ese nombre y el monto actual.")
                return
            
            # Se actualiza el monto del producto.
            self.conexion.cursor.execute("UPDATE productos SET precio_compra = ? WHERE nombre_producto = ? AND precio_compra = ?",(precio_compra,nombre_producto,monto_actual))
            # Se suben los cambios a la base de datos.
            self.conexion.conn.commit()
            print("Monto total de los productos actualizado exitosamente.")

        # Manejo de errores.
        except Exception as error:
            print(f"Error en el programa : {error}.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}.")
    
    def modificar_fecha(self):
        try:

            # Entrada de usuario.
            nombre_producto = str(input("Ingresa el nombre del producto : ")).strip()
            fecha_actual = str(input("Ingresa la fecha actual de los productos: ")).strip()
            fecha_ingreso = str(input("Ingresa la fecha de ingreso de los productos: ")).strip()

                        # Se verifica si la fecha no sea igual al anterior.
            if fecha_actual == fecha_ingreso:
                print("La fecha de ingreso nueva es igual a la actual, por favor ingresar una nueva.")
                return
            # Validacion de campos.
            elif not all([nombre_producto,fecha_actual,fecha_ingreso]):
                print("Los campos deben estar completos.")
                return
            try:
                # Uso del modulo para verificar fechas validas.
                datetime.strptime(fecha_ingreso, "%d/%m/%Y")
            # Manejo de errores.
            except ValueError:
                print("La fecha no es valida, por favor ingresar nuevamente.")
                return

            # Se busca el nombre del producto como su fecha de ingreso en la base de datos.
            self.conexion.cursor.execute("SELECT 1 FROM productos WHERE nombre_producto = ? AND fecha_ingreso = ?",(nombre_producto,fecha_actual))
            if not self.conexion.cursor.fetchone():
                print("No se encontró el producto con ese nombre y la fecha actual.")
                return

            # Se actualiza la fecha de ingreso del producto.
            self.conexion.cursor.execute("UPDATE productos SET fecha_ingreso = ? WHERE nombre_producto = ? AND fecha_ingreso = ?",(fecha_ingreso,nombre_producto,fecha_actual))
            # Se suben los cambios a la base de datos.
            self.conexion.conn.commit()
            print("Fecha de ingreso del producto actualizado exitosamente.")

        # Manejo de errores.
        except Exception as error:
            print(f"Error en el programa : {error}.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos : {error}.")

    # Salida de las modificaciones de inventario.
    def salir_programa(self):
        exit()

