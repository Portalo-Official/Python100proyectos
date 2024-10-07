
def printElements(collection:list):
    """
    Realiza la impresion por consola de los elementos de una lista
    Raise:
        TypeError: Cuando el parametro no es una instancia de la clase list
    """
    if not isinstance(collection, list):
        raise TypeError("El valor por parametro no es una lista")
    for element in collection:
        print(element)


if __name__=="__main__":
    # Maneras de iniciar una lista
    numeros:list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numeros= list(range(11))
    numeros = [i for i in range(1, 11)]
    # printElements(numeros)

    suma = sum(numeros)
    print(f"\nLa suma de todos los números en la lista es: {suma}")
    pares = [numero for numero in numeros if numero % 2 == 0]
    print(f"\nNúmeros pares en la lista: {pares}")

    #Añadir una los elementos de una lista
    nuevos_numeros = [11, 12, 13]
    numeros.extend(nuevos_numeros)
    print(f"\nLista después de añadir nuevos números: {numeros}")

    print("")
    lista2 = [23, -4, 34, 5, -7, 1]
    print(f"lista desordenada: {lista2}")
    lista2.sort()
    print(f"lista ordenada: {lista2}")