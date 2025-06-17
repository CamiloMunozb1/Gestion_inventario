# 📦 Gestor de Inventario - Proyecto en Python

Este es un sistema de gestión de inventario desarrollado en Python, con almacenamiento local usando SQLite. Permite registrar, consultar, modificar y eliminar productos de una base de datos de forma sencilla desde la terminal.

## 🧠 Funcionalidades

-  Registro de nuevos productos (nombre, cantidad, proveedor, precio, fecha).
-  Modificación de información por campos (nombre, cantidad, proveedor, precio, fecha).
-  Eliminación de productos mediante el nombre.
-  Visualización de productos almacenados.
-  Validaciones estrictas para evitar datos duplicados o inválidos.

## 🛠️ Tecnologías Usadas

- **Python 3.x**
- **SQLite3** (base de datos local)
- Sistema modular con clases por responsabilidad (`IngresoProductos`, `CambiosElementos`, etc.)

## ⚙️ Requisitos

- Python 3.7 o superior
- Sistema operativo con terminal (Windows, Linux, macOS)

## 🚀 Cómo usar

1. Clona el repositorio o descarga los archivos.
2. Asegúrate de tener la ruta correcta a tu base de datos en `index.py`:
3. Ejecutar el programa desde consola.

## 🧼 Validaciones incluidas

- No se aceptan campos vacíos.
- Nombres de producto no pueden repetirse.
- Las cantidades y precios deben ser mayores que cero.
- No se permite actualizar si los datos nuevos son idénticos a los actuales.

## Autor

Juan Camilo Muñoz Bautista.

## Licencia

Este proyecto esta bajo una licencia MIT.
