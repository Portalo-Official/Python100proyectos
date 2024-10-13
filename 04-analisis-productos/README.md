# Ejercicio Python: Análisis de Productos

Este repositorio contiene un ejercicio en Python relacionado con la manipulación de datos de productos vendidos. El objetivo es aplicar funciones de orden superior como `map()`, `filter()`, `reduce()` y `max()` junto con funciones lambda para realizar diferentes análisis sobre los productos.

## Descripción del Ejercicio

### Tareas a Realizar:

1. **Calcular el precio total por producto**:
   - Para cada producto, se calcula el total multiplicando la cantidad vendida por el precio por unidad.
   - Se utiliza `map()` junto con una función `lambda` para generar una nueva lista que contenga el nombre del producto y su total de ventas.

2. **Filtrar productos cuyo total supere un umbral**:
   - Filtra aquellos productos cuyo total (cantidad vendida * precio) sea superior a un umbral de 10,000.
   - Se utiliza `filter()` con una función `lambda` para obtener los productos que cumplan este criterio.

3. **Calcular el total de todas las ventas combinadas**:
   - Suma el total de todas las ventas de todos los productos.
   - Se utiliza `reduce()` para acumular y calcular el total de las ventas.

4. **Encontrar el producto más caro**:
   - Encuentra el producto con el precio por unidad más alto utilizando `max()` y una función `lambda`.

5. **Encontrar el producto más vendido (en cantidad)**:
   - Encuentra el producto con la mayor cantidad vendida utilizando `max()` y una función `lambda`.

## Ejemplo de Datos:

```python
productos_datos = [
    ("Laptop", 25, 1200),
    ("Smartphone", 80, 800),
    ("Tablet", 50, 600),
    ("Monitor", 40, 300),
    ("Teclado", 100, 50),
    ("Ratón", 120, 40),
    ("Cámara", 30, 900),
    ("Impresora", 45, 150),
    ("Parlantes", 60, 100),
    ("Cargador", 200, 20),
    ("Disco Duro", 150, 100),
    ("Memoria USB", 300, 15),
    ("Smartwatch", 70, 250),
    ("Consola de Juegos", 35, 500),
    ("Televisor", 20, 2000),
    ("Router", 75, 120),
    ("Auriculares", 90, 80),
    ("Microondas", 22, 350),
    ("Refrigerador", 15, 2200),
    ("Lavadora", 10, 1800)
]

## Requisitos del Sistema:

- Python 3.x
- Biblioteca functools (para la función reduce, que está incluida en Python).

## Instrucciones para Ejecutar:

1. Clona este repositorio:

   git clone https://github.com/tu_usuario/tu_repositorio.git

2. Navega al directorio del proyecto:

   cd tu_repositorio

3. Ejecuta el script principal:

   python main.py

## Autor:
- Nombre: Santiago Miguez

