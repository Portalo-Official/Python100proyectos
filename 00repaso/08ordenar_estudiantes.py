from functools import reduce
"""
Ejercicio: Ordenar un Diccionario de Estudiantes por Calificaciones

Objetivo: El objetivo de este ejercicio es que aprendas a manipular 
diccionarios utilizando funciones lambda, y a ordenar y filtrar datos 
usando funciones de orden superior como sorted(), filter() y reduce(). 
Trabajarás con un diccionario que contiene estudiantes y sus calificaciones,
 realizando diferentes operaciones para analizar los datos.

Tareas del ejercicio:

 1) Ordenar a los estudiantes por sus calificaciones de mayor a menor:
   - Utilizarás la función sorted() junto con una función lambda para ordenar 
     a los estudiantes basándote en sus calificaciones.

 2) Filtrar estudiantes con calificaciones mayores a 80:
   - Utilizarás filter() para crear una lista de estudiantes que 
     tengan una calificación superior a 80.

 3) Calcular el promedio de calificaciones:
   - Usarás la función reduce() para calcular el promedio de todas
     las calificaciones de los estudiantes.

 4)Encontrar el estudiante con la calificación más baja:
   - Emplearás min() junto con una función lambda para encontrar 
     al estudiante con la calificación más baja.

Explicación del ejercicio:
DICCIONARIOS: Utilizarás un diccionario donde cada clave será el nombre del 
estudiante y el valor será su calificación.
FUNCIONES LAMBDA: Te ayudarán a definir pequeñas funciones anónimas para 
trabajar con los valores dentro de las funciones de orden superior.
ORDENAMIENTO: Aprenderás a usar la función sorted() para ordenar elementos de 
un diccionario según un criterio.
FILTRO Y REDUCCIÓN: Practicarás filtrando datos con filter() y calculando 
acumulaciones con reduce().
Este ejercicio es fundamental para que entiendas cómo manipular y analizar 
datos de manera eficiente en Python, habilidades clave para análisis y procesamiento de datos.
"""
# Diccionario de estudiantes con sus calificaciones
estudiantes = {
    "Juan": 85,
    "María": 92,
    "Pedro": 78,
    "Piedad": 62,
    "Ana": 95,
    "Luis": 88
}

# 1. Ordenar a los estudiantes por sus calificaciones de mayor a menor usando sorted() y una función lambda
estudiantes_ordenados = sorted(estudiantes.items(), key= lambda x: x[1], reverse=True)
print(f"Estudiantes ordenados\n{estudiantes_ordenados}")

# 2. Filtrar estudiantes con calificaciones mayores a 80 usando filter() y una función lambda
estudiantes_mayor_80 = list(filter(lambda x: x[1]>80, estudiantes.items()))
print(f"Estudiantes con puntuacion amyor 80\n{estudiantes_mayor_80}")

# 3. Calcular el promedio de calificaciones usando reduce()


# 4. Encontrar el estudiante con la calificación más baja usando min() y una función lambda
