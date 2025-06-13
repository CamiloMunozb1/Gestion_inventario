from funcionalidad.Ingreso_nuevo import IngresoDB,IngresoProductos
from funcionalidad.modificacion_elemento import IngresoDB,CambiosElementos
from funcionalidad.vizualizar import IngresoDB,MostrarInventario
from funcionalidad.eliminar_elemento import IngresoDB,EliminarElementos

ruta_db = r"TU_BASE_DATOS"
conexion = IngresoDB(ruta_db)

while True:
    print("""
        Bienvenido al gestor de inventario:
            1. Ingreso de inventario.
            2. Modificar un articulo.
            3. Ver inventario ingresado.
            4. Eliminar productos.
            5. Salir
        """)
    try:
        usuario = str(input("Ingresa la opcion que desees: ")).strip()
        if not usuario:
            print("El campo debe estar completo.")
            break
        elif usuario == "1":
            productos = IngresoProductos(conexion)
            productos.ingresos_productos()
        elif usuario == "2":
            modificacion = CambiosElementos(conexion)
            modificacion.eleccion_usuario()
        elif usuario == "3":
            vizualiar = MostrarInventario(conexion)
            vizualiar.motrar_inventario()
        elif usuario == "4":
            eliminar = EliminarElementos(conexion)
            eliminar.inventario_eliminar()
        elif usuario == "5":
            print("Hasta el proximo inventario.")
            break
        else:
            print("Ingresa un valor numero del 1 al 5.")

        input("\nPresiona enter para continuar...")
    
    except ValueError:
        print("Error de digitacion, volver a intentar.")
    except Exception as error:
        print(f"Error en el programa : {error}.")