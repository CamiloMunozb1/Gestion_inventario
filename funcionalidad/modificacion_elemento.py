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
        self.opciones_usuario()

    def opciones_usuario(self):
        self.opciones = {
            "1" : self.opcion_uno,
            "2" : self.opcion_dos,
            "3" : self.opcion_tres,
            "4" : self.opcion_cuatro,
            "5" : self.opcion_cinco,
            "6" : self.opcion_seis
        }
    
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
                self.mostar_opciones()
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
