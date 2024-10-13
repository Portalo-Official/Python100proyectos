"""
Ejercicio: Análisis de Ventas
Vamos a seguir con un ejercicio que te ayudará a reforzar tu habilidad para analizar
 datos usando funciones lambda, map(), filter(), y reduce() en un contexto de ventas.

Enunciado del Ejercicio: Análisis de Ventas
Objetivo: Trabajarás con una lista de ventas que contiene tuplas con el nombre del 
vendedor, el número de unidades vendidas y el precio por unidad. Usarás map(),
filter(), reduce() y funciones lambda para realizar diferentes cálculos.

Tareas del ejercicio:
1. Calcular el total de ingresos por cada vendedor usando map() y una función lambda.
2. Filtrar las ventas que superen un umbral de ingresos totales usando filter().
3. Calcular los ingresos totales de todos los vendedores usando reduce().
4. Encontrar al vendedor con los ingresos más altos usando max() y una función lambda.
"""
from functools import reduce

# Lista de ventas: (vendedor, unidades vendidas, precio por unidad)
ventas = [
    ("Carlos", 100, 20),
    ("Ana", 120, 25),
    ("Luis", 80, 30),
    ("María", 150, 22),
    ("Juan", 90, 18)
]

# 1. Calcular el total de ingresos por cada vendedor usando map() y una función lambda.
ingresos = list(map(lambda venta: (venta[0],venta[1]*venta[2]), ventas))
print("\nIngresos por vendedor")
print(ingresos)

# 2. Filtrar las ventas que superen el umbral de 2500 de ingreso totales usando filter().
ingresos_superior_2500 = list(filter(lambda ingreso: ingreso[1]>2500, ingresos))
print("\nIngresos mayores que 2500:")
print(ingresos_superior_2500)

# 3. Calcular los ingresos totales de todos los vendedores usando reduce().
total_ingresos= reduce(lambda total,ingreso: total+ ingreso[1],ingresos, 0)
print("\nTotal de ingresos:")
print(total_ingresos)

# 4. Encontrar al vendedor con los ingresos más altos usando max() y una función lambda.
maximo_ingreso= max(ingresos, key=lambda x: x[1])
print(f"\nVendedor con mayor ingreso: {maximo_ingreso}")