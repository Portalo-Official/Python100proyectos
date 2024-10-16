"""
# Ejercicio: Gestión de Inventario

## Objetivo:
Implementar un sistema básico de gestión de inventario para una tienda. Deberás calcular el valor total del inventario, filtrar los productos con bajo stock, y actualizar el inventario después de cada venta.

## Tareas del ejercicio:

### 1. Definir una clase `Producto`:
   - Esta clase tendrá atributos como el nombre, la cantidad disponible, el precio por unidad, y métodos para realizar ventas y mostrar información del producto.

### 2. Crear una clase `Inventario`:
   - Esta clase manejará una lista de productos y tendrá métodos para:
     - Calcular el valor total del inventario.
     - Filtrar productos con bajo stock (por ejemplo, menos de 10 unidades).
     - Actualizar la cantidad disponible después de una venta.
     - Mostrar el producto con el valor total más alto en el inventario.

### 3. Simular ventas y actualizar el inventario:
   - Después de cada venta, actualiza la cantidad disponible de productos en el inventario.

## Datos iniciales:

Utiliza los siguientes productos para poblar tu inventario:

productos_iniciales = [
    {"nombre": "Laptop", "cantidad": 25, "precio": 1200},
    {"nombre": "Smartphone", "cantidad": 80, "precio": 800},
    {"nombre": "Tablet", "cantidad": 50, "precio": 600},
    {"nombre": "Monitor", "cantidad": 40, "precio": 300},
    {"nombre": "Teclado", "cantidad": 100, "precio": 50},
    {"nombre": "Ratón", "cantidad": 120, "precio": 40},
    {"nombre": "Cámara", "cantidad": 30, "precio": 900},
    {"nombre": "Impresora", "cantidad": 45, "precio": 150}
]

## Tareas adicionales (opcional):
1. Implementar un sistema de descuentos para algunos productos.
2. Implementar una opción para agregar productos nuevos al inventario.
3. Crear un reporte del inventario mostrando productos ordenados por valor total en inventario.
"""