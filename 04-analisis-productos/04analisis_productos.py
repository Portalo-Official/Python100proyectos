"""
Ventas de productos.

Tareas del ejercicio:

1. Calcular el precio total por producto: Para cada producto, calcula el total 
   multiplicando la cantidad vendida por el precio por unidad. Usa map() y una función 
   lambda para generar una nueva lista con el nombre del producto y su total.

2. Filtrar productos cuyo total supere un umbral: Filtra aquellos productos cuyo total
   (cantidad * precio) sea superior a 10,000 usando filter() y una función lambda.

3. Calcular el total de todos los productos vendidos: Suma el total de todas las ventas
   (cantidad * precio) de todos los productos combinados. Usa reduce() para este cálculo.

4. Encontrar el producto más caro: Encuentra el producto con el precio más alto por unidad
   utilizando max() y una función lambda.

5. Encontrar el producto más vendido (en cantidad): Encuentra el producto con la mayor
   cantidad vendida utilizando max() y una función lambda.

Detalles adicionales del ejercicio:

1. Total por producto: Multiplica la cantidad por el precio para obtener el total.
2. Umbral de 10,000: Usa este umbral como referencia para filtrar los productos más vendidos.
3. Uso de reduce(): Úsalo para acumular el total de todos los productos vendidos.
4. Uso de max(): Encuentra tanto el producto más caro como el más vendido usando el 
   key adecuado en las funciones lambda.

Soluciones de salida:
 1.
  [('Laptop', 30000), ('Smartphone', 64000), ('Tablet', 30000), ...]
 2.
  [('Laptop', 30000), ('Smartphone', 64000), ('Tablet', 30000), ...]
 3. 
  Total de ingresos de todos los productos: 515,000
 4.
  Producto más caro: ('Refrigerador', 2200)
 5.
  Producto más vendido: ('Memoria USB', 300)
"""
from productos import productos_datos as data


# 1. Calcular el precio total por producto: Para cada producto, calcula el total 
#    multiplicando la cantidad vendida por el precio por unidad. Usa map()
total_por_producto = list(map(lambda x: (x[0],x[1]*x[2]), data))
# print(f"La venta por producto es {total_por_producto}")

#2. Filtra aquellos productos cuyo total (cantidad * precio) 
#  sea superior a 10,000 usando filter() y una función lambda.
prodcutos_mayor_10_000 = list(filter(lambda x: x[1]>10_000, total_por_producto))
print(f"Productos matyores a 10000\n{prodcutos_mayor_10_000}")


