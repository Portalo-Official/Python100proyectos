from functools import reduce

# Lista inicial de numeros
numeros = [numero for numero in range(1,23,1)]

print(numeros)

#1. Elevar cada numero al cuadrado usando map() y una funcion lambda
cuadrado  = list(map(lambda x: x**2, numeros))
print(cuadrado)

"""
2. Filtrar los numeros impares de la lista original usando filter() 
y una funcion lambda
"""
numeros_impares = list(filter(lambda x:x%2!=0, numeros))
print(numeros_impares)

#3. Calcular la suma de todos los numeros usando reduce()
sumatorio = reduce(lambda x,y: x+y, numeros)
print(sumatorio)

# 4. Crear una lista de números pares multiplicados por 2
num_pares_x2 = list(map(lambda x: x*2, filter(lambda x: x%2==0, numeros)))
print(num_pares_x2)

# 5. Encontrar el número mayor usando reduce()
numero_mayor = reduce(lambda x,y: x if x>y else y, numeros)
print(numero_mayor)
# 6. Generar una lista de tuplas con cada número y su cuadrado
tuplas_cuadrado = list(map(lambda x: (x, x**2), numeros))
print(tuplas_cuadrado)